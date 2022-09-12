import unittest
from function import sum_range


class SumRangeTest(unittest.TestCase):

    def test_positive_straight_test(self):
        self.assertEqual(
            15,
            sum_range(1, 5)
        )

    def test_positive_reverse(self):
        self.assertEqual(
            52,
            sum_range(10, 3)
        )

    def test_negative_type(self):
        with self.assertRaises(TypeError):
            sum_range(1, 't')

    def test_equals(self):
        self.assertEqual(
            6,
            sum_range(6, 6)
        )

    def test_float(self):
        with self.assertRaises(TypeError):
            sum_range(4.1, 6.3)

    def test_negative(self):
        self.assertEqual(
            -6,
            sum_range(-3, 0)
        )
