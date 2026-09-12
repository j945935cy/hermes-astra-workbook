"""Chapter-local regressions. References are not model outputs."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent

class FeeRegressionTests(unittest.TestCase):
    def test_reference_and_four_mutations(self):
        source = (HERE / "reference/fee.py").read_text(encoding="utf-8")
        variants = {
            "reference": source,
            "above_only": source.replace("quantity >= 3", "quantity > 3"),
            "exact_three_only": source.replace("quantity >= 3", "quantity == 3"),
            "all_discounted": source.replace("quantity >= 3", "quantity >= 1"),
            "boolean_accepted": source.replace("type(quantity) is not int", "not isinstance(quantity, int)"),
        }
        for name, implementation in variants.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "fee.py").write_text(implementation, encoding="utf-8")
                shutil.copyfile(HERE / "reference/test_fee.py", root / "test_fee.py")
                shutil.copyfile(HERE / "starter/acceptance.py", root / "acceptance.py")
                for args in [["-m", "unittest", "-v"], ["acceptance.py"]]:
                    result = subprocess.run([sys.executable, "-B", *args], cwd=root,
                                            text=True, capture_output=True)
                    if name == "reference":
                        self.assertEqual(result.returncode, 0, result.stderr)
                    else:
                        self.assertNotEqual(result.returncode, 0, name)

if __name__ == "__main__":
    unittest.main()
