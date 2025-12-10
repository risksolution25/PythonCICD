import unittest
from app import calculate

class TestCalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(2, 3, "add"), 5)

    def test_subtract(self):
        self.assertEqual(calculate(5, 2, "subtract"), 3)

    def test_multiply(self):
        self.assertEqual(calculate(4, 3, "multiply"), 12)

    def test_divide(self):
        self.assertEqual(calculate(10, 2, "divide"), 5)

    def test_divide_by_zero(self):
        self.assertEqual(calculate(10, 0, "divide"), "Error: divide by zero")

    def test_invalid(self):
        self.assertEqual(calculate(10, 2, "nope"), "Invalid operation")

if __name__ == "__main__":
    unittest.main()
