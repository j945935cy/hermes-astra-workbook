import unittest
from fee import quote

class FeeTests(unittest.TestCase):
    def test_three_regular_tickets_receive_discount(self):
        self.assertEqual(quote("regular", 3), 810)

    def test_student_threshold(self):
        self.assertEqual(quote("student", 3), 540)
        self.assertEqual(quote("student", 4), 720)

    def test_before_threshold(self):
        self.assertEqual(quote("regular", 2), 600)
        self.assertEqual(quote("student", 2), 400)

    def test_invalid_inputs(self):
        for kind, quantity in [("vip", 1), ("regular", 0), ("student", -1),
                               ("regular", 1.5), ("student", True), ("regular", "3")]:
            with self.subTest(kind=kind, quantity=quantity):
                with self.assertRaises(ValueError):
                    quote(kind, quantity)

if __name__ == "__main__":
    unittest.main()
