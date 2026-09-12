"""Offline period-2 contract regressions; never calls a model."""
import csv
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent

class Period2Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "case"
        shutil.copytree(HERE / "starter", self.root)
        shutil.copytree(HERE / "reference/output", self.root / "output")

    def run_verify(self):
        return subprocess.run([sys.executable, "-B", str(self.root / "verify.py")],
                              text=True, capture_output=True)

    def rows(self):
        with (self.root / "output/actions.csv").open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return reader.fieldnames, list(reader)

    def save(self, fields, rows):
        with (self.root / "output/actions.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_approved_reference(self):
        result = self.run_verify()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("human review still required", result.stdout)

    def test_empty_output_rejected(self):
        shutil.rmtree(self.root / "output")
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_wrong_date_rejected(self):
        fields, rows = self.rows()
        rows[2]["due"] = "2026-10-13"
        self.save(fields, rows)
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_missing_new_task_rejected(self):
        fields, rows = self.rows()
        self.save(fields, rows[:-1])
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_wrong_source_mapping_rejected(self):
        fields, rows = self.rows()
        rows[2]["sources"] = "tasks.csv:G04;notes.md:N03"
        self.save(fields, rows)
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_unknown_status_rejected(self):
        fields, rows = self.rows()
        rows[-1]["status"] = "unknown"
        self.save(fields, rows)
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_duplicate_rejected(self):
        fields, rows = self.rows()
        self.save(fields, rows + [rows[0]])
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_changed_source_rejected(self):
        p = self.root / "input/tasks.csv"
        p.write_text(p.read_text(encoding="utf-8").replace("整理回饋問卷", "偷偷換題"), encoding="utf-8")
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_missing_document_rejected(self):
        (self.root / "output/README.md").unlink()
        self.assertNotEqual(self.run_verify().returncode, 0)

    def test_prepare_rejects_missing_required_files_before_creation(self):
        for missing in ('input/notes.md', 'approved-baseline.md'):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as temp:
                base = Path(temp)
                script = base / 'prepare_period2.py'
                shutil.copyfile(HERE / 'prepare_period2.py', script)
                shutil.copytree(HERE / 'starter', base / 'starter')
                (base / 'starter' / missing).unlink()
                target = base / 'destination'
                result = subprocess.run([sys.executable, '-B', str(script), str(target)], text=True, capture_output=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn('STOP:', result.stderr)
                self.assertFalse(target.exists(), 'Missing inputs must not create a partial destination')

    def test_prepare_rejects_symlink_source_before_creation(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            script = base / 'prepare_period2.py'
            shutil.copyfile(HERE / 'prepare_period2.py', script)
            shutil.copytree(HERE / 'starter', base / 'starter')
            source = base / 'starter/input/notes.md'
            outside = base / 'outside.md'
            source.rename(outside)
            source.symlink_to(outside)
            target = base / 'destination'
            result = subprocess.run([sys.executable, '-B', str(script), str(target)], text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertFalse(target.exists())

    def test_prepare_guard(self):
        parent = Path(self.tmp.name)
        script = HERE / "prepare_period2.py"
        def run(path):
            return subprocess.run([sys.executable, "-B", str(script), str(path)], text=True, capture_output=True)
        target = parent / "new period with spaces"
        self.assertEqual(run(target).returncode, 0)
        self.assertTrue((target / "verify.py").is_file())
        self.assertFalse((target / "output").exists())
        before = (target / "input/tasks.csv").read_bytes()
        self.assertNotEqual(run(target).returncode, 0)
        self.assertEqual((target / "input/tasks.csv").read_bytes(), before)
        self.assertNotEqual(run(parent / "absent" / "child").returncode, 0)
        link = parent / "link"
        link.symlink_to(parent, target_is_directory=True)
        self.assertNotEqual(run(link / "child").returncode, 0)
        broken = parent / "broken"
        broken.symlink_to(parent / "missing")
        self.assertNotEqual(run(broken).returncode, 0)

if __name__ == "__main__":
    unittest.main()
