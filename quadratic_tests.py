from unittest import TestCase
from quadratic import find_roots
import unittest


class QuadraticTest(unittest.TestCase):

    # Test solving a quadratic equation

    def test_one_root(self):
        self.assertEqual(find_roots(2, 4, 2),-1.0)

    def test_d_equal_zero(self):
        self.assertEqual(find_roots(1, 2, 1), (-1.0))

    def test_a_equal_zero(self):
        self.assertEqual(find_roots(0, 4, 2), None)

    def test_two_root(self):
        self.assertEqual(find_roots(1, 6, 3), (-0.5505102572168221, -5.449489742783178))
        self.assertEqual(find_roots(1, 5, 1), (-0.20871215252208009, -4.7912878474779195))

    def test_d_less_than_zero(self):
        self.assertEqual(find_roots(2, 4, 10), "NO ROOTS")
        self.assertEqual(find_roots(5, 4, 1), "NO ROOTS")


if __name__ == '__main__':
    unittest.main()
