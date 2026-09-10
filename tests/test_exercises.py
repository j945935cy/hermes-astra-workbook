"""Exercise exact book snippets in disposable copies, never against reader output."""
from pathlib import Path
from functools import partial
import ast
import csv
import io
import json
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]

class ExerciseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="companion-test-")
        self.addCleanup(self.temp.cleanup)
        self.lab = Path(self.temp.name) / "lab"

    def starter(self, chapter):
        shutil.copytree(ROOT / f"examples/ch{chapter:02}/starter", self.lab)

    def run_python(self, *args, ok=True):
        result = subprocess.run([sys.executable, "-B", *args], cwd=self.lab,
                                capture_output=True, text=True, timeout=30)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def test_ch10_published_verifier_positive_and_mutations(self):
        self.starter(10)
        output = self.run_python("test_verify.py")
        lines = output.splitlines()
        self.assertTrue(all(line.startswith("OK ") for line in lines), output)
        self.assertIn("OK 正確八列: exit=0", output)
        self.assertIn("OK 正確 R9 衝突優先: exit=0", output)
        self.assertIn("OK R9 錯誤先去重分流: exit=1", output)
        print(f"ch10: {len(lines)} published verifier scenarios passed")

    def test_ch10_missing_outputs_rejected(self):
        self.starter(10)
        self.assertIn("FileNotFoundError", self.run_python("verify.py", ok=False))

    def test_ch12_baseline_and_observed_unspecified_input(self):
        self.starter(12)
        self.assertEqual(self.run_python("app.py").strip(), "林青｜2 位")
        self.assertIn("Ran 1 test", self.run_python("-m", "unittest", "-v"))
        self.assertEqual(self.run_python("-c", 'from app import make_label; print(repr(make_label("", 0)))').strip(), "'｜0 位'")

    def test_ch12_regression_catches_removed_trim(self):
        self.starter(12)
        file = self.lab / "app.py"
        file.write_text(file.read_text().replace("name.strip()", "name"), encoding="utf-8")
        self.assertIn("AssertionError", self.run_python("-m", "unittest", "-v", ok=False))

    def test_ch13_red_then_reference_green(self):
        self.starter(13)
        self.assertIn("900 != 810", self.run_python("-m", "unittest", "-v", ok=False))
        shutil.copyfile(ROOT / "examples/ch13/reference/fee.py", self.lab / "fee.py")
        self.assertIn("Ran 1 test", self.run_python("-m", "unittest", "-v"))
        self.assertIn("ACCEPTED: fee contract", self.run_python("acceptance.py"))

    def test_ch13_acceptance_rejects_mutants(self):
        self.starter(13)
        code = (ROOT / "examples/ch13/reference/fee.py").read_text()
        for old, new in [("quantity >= 3", "quantity > 3"),
                         ("quantity >= 3", "quantity == 3"),
                         ("quantity >= 3", "quantity >= 1"),
                         ("type(quantity) is not int", "not isinstance(quantity, int)")]:
            with self.subTest(new=new):
                self.assertIn(old, code)
                (self.lab / "fee.py").write_text(code.replace(old, new), encoding="utf-8")
                self.assertIn("AssertionError", self.run_python("acceptance.py", ok=False))

    def test_ch14_real_http_success_missing_page_and_shutdown(self):
        self.starter(14)
        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(self.lab)))
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}/"
        try:
            with urlopen(url, timeout=5) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(response.read(), (self.lab / "index.html").read_bytes())
            with self.assertRaises(HTTPError) as error:
                urlopen(url + "missing-page", timeout=5)
            self.assertEqual(error.exception.code, 404)
            error.exception.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)
        self.assertFalse(thread.is_alive())
        with self.assertRaises(OSError):
            urlopen(url, timeout=1)

    def test_ch15_source_and_modified_source(self):
        self.starter(15)
        output = self.run_python("verify_source.py")
        self.assertIn("{'W02': 2}", output)
        self.assertIn("['W03']", output)
        path = self.lab / "sessions.csv"
        path.write_text(path.read_text().replace("8,10,小岳", "8,8,小岳"), encoding="utf-8")
        self.assertIn("source differs", self.run_python("verify_source.py", ok=False))

    def test_ch17_literal_review_only_not_sdk_execution(self):
        self.starter(17)
        tree = ast.parse((self.lab / "server.py").read_text())
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
        self.assertEqual([f.name for f in functions], ["list_records"])
        result = next(n for n in functions[0].body if isinstance(n, ast.Return))
        self.assertIsNotNone(result.value)
        assert result.value is not None
        records = ast.literal_eval(result.value)
        self.assertEqual(records, [dict(id="R01", title="整理器材", owner="小河", status="open"),
                                   dict(id="R02", title="確認投影", owner="小杉", status="done")])
        self.assertEqual([r["id"] for r in records if r["status"] == "open"], ["R01"])
        records[0]["status"] = "done"
        self.assertEqual([r for r in records if r["status"] == "open"], [])

    def reference18(self):
        self.starter(18)
        shutil.copytree(ROOT / "examples/ch18/reference/output", self.lab / "output")

    def test_ch18_reference_acceptance(self):
        self.reference18()
        self.assertIn("human review still required", self.run_python("verify.py"))

    def test_ch18_missing_output_rejected(self):
        self.starter(18)
        self.assertIn("FileNotFoundError", self.run_python("verify.py", ok=False))

    def test_ch18_output_mutations_rejected(self):
        self.reference18()
        path = self.lab / "output/actions.csv"
        original = path.read_text()
        changes = [original.replace("小安,待確認,todo", "小安,2026-10-11,todo"),
                   "\n".join(line for line in original.splitlines() if not line.startswith("G03,")) + "\n",
                   original + original.splitlines()[1] + "\n",
                   original.replace(",doing,", ",unknown,"),
                   original.replace("notes.md:N02", "notes.md:N01")]
        for index, changed in enumerate(changes):
            with self.subTest(mutation=index):
                self.assertNotEqual(changed, original)
                path.write_text(changed, encoding="utf-8")
                self.assertIn("action rows differ", self.run_python("verify.py", ok=False))
        path.write_text(original, encoding="utf-8")
        self.run_python("verify.py")

    def test_ch18_source_and_missing_document_rejected(self):
        self.reference18()
        path = self.lab / "input/tasks.csv"
        original = path.read_text()
        path.write_text(original.replace(",doing", ",done"), encoding="utf-8")
        self.assertIn("source task fixture changed", self.run_python("verify.py", ok=False))
        path.write_text(original, encoding="utf-8")
        (self.lab / "output/report.md").unlink()
        self.run_python("verify.py", ok=False)

    def test_prepare_missing_source_and_dangling_symlink_stop(self):
        # No source fixture or destination from the real checkout is mutated.
        clone = Path(self.temp.name) / "checkout"
        shutil.copytree(ROOT / "scripts", clone / "scripts")
        shutil.copyfile(ROOT / "extraction-manifest.json", clone / "extraction-manifest.json")
        command = [sys.executable, "-B", str(clone / "scripts/prepare.py"), "13", str(self.lab)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.lab.exists())
        self.lab.symlink_to(Path(self.temp.name) / "absent")
        command[2] = str(ROOT / "scripts/prepare.py")
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(self.lab.is_symlink())
        self.assertFalse(self.lab.exists())

if __name__ == "__main__":
    unittest.main()
