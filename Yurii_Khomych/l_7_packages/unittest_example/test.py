import unittest
from fractions import Fraction

from my_sum import my_sum_func


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum_func(data)
        self.assertEqual(result, 6, "Should be 6")

    # def test_list_fraction(self):
    #     """
    #     Test that it can sum a list of fractions
    #     """
    # data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    # result = my_sum_func(data)
    # self.assertEqual(1, result)

    # def test_func_false(self):
    #     res = func_false()
    #     self.assertFalse(res)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            my_sum_func(data)


if __name__ == "__main__":
    unittest.main()
