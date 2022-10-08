import unittest
from main import *


class TestCalcSault(unittest.TestCase):
    def test_calc_sault_returns_mass(self):
        self.assertEqual(calc_salt(1000), 15)
        self.assertEqual(calc_salt(2000), 30)
        self.assertEqual(calc_salt(500), 7)

    def test_calc_sault_returns_integer(self):
        self.assertIsInstance(calc_salt(1000), int)


if __name__ == "__main__":
    unittest.main()
