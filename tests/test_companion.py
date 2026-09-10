"""Offline companion regression tests; no model or Hermes configuration."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PrepareTests(unittest.TestCase):
    def test_prepare_preserves_source_and_refuses_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / "new lab"
            command = [sys.executable, "-B", str(ROOT / "scripts/prepare.py"), "13", str(dest)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((dest / "fee.py").read_bytes(), (ROOT / "examples/ch13/starter/fee.py").read_bytes())
            before = (dest / "fee.py").read_bytes()
            again = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertEqual((dest / "fee.py").read_bytes(), before)

class IntegrityTests(unittest.TestCase):
    def test_manifest_detects_mutated_fixture(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "copy"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            command = [sys.executable, "-B", str(ROOT / "scripts/verify_assets.py"), "--root", str(root)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            source = root / "examples/ch10/starter/registrations.csv"
            source.write_text(source.read_text().replace("周舟", "錯名"), encoding="utf-8")
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("registrations.csv", result.stderr + result.stdout)

if __name__ == "__main__":
    unittest.main()
