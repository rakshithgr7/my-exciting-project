import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.add(3, 4)
        self.assertEqual(result, 9)

    def test_subtraction(self):
        result = self.calc.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiplication(self):
        result = self.calc.multiply(2, 5)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
