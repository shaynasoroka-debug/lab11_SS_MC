# https://github.com/shaynasoroka-debug/lab11_SS_MC.git
# Partner 1: Shayna Soroka
# Partner 2: Maya Crecos

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -4), -5)
        self.assertEqual(add(7, -2), 5)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(7, 0), 7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(0, 7), 0)
        self.assertEqual(mul(-5, 2), -10)

    def test_divide(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, -9), -3)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(div(0, 5))

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(100, 10), 0.5)
        self.assertAlmostEqual(logarithm(math.e, math.e), 1.0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)
    

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ValueError):
            hypotenuse(-3, 4)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5.5, 2.5), 6.041522986797286)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
# Do not touch this
if __name__ == "__main__":
    unittest.main()