import unittest
import sys, os

sys.path.append(os.getcwd())
from tmp_sem2.main import *


class TestCalc(unittest.TestCase):
    def test_calc_sault_returns_mass(self):
        self.assertEqual(calc_salt(1000), 15)
        self.assertEqual(calc_salt(2000), 30)
        self.assertEqual(calc_salt(500), 7)

    def test_calc_sault_returns_integer(self):
        self.assertIsInstance(calc_salt(1000), int)

    def test_calc_sault_gets_string_returns_int(self):
        self.assertIsInstance(calc_salt(1000), int)
        self.assertEqual(calc_salt('1000'), 15)

    def test_calc_sault_gets_incorrect_string_returns_zero(self):
        self.assertEqual(calc_salt('abc'), 0)


class TestCalculator(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator()

    # Each test method starts with the keyword test_
    def test_add(self):
        self.assertEqual(self.calculator.add(4,7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,2), 5)


if __name__ == '__main__':
    unittest.main()
