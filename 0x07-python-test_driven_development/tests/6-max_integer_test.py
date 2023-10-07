import unittest
max_integer = __import__('6-max_integer').max_integer
"""
this module with purpose to test all functions of module
6-max_integer.py
"""


class TestMaxInteger(unittest.TestCase):
    """
    implement test cases
    """
    # test_01
    def test_max_of_int_list(self):
        """ test list of int"""
        res = max_integer([1, 5, 6])
        self.assertEqual(res, 6)

    # test_02
    def test_empty_argument(self):
        """ test call function en empty arg"""
        res = max_integer()
        self.assertEqual(res, None)

    # test_03
    def test_max_of_empty_list(self):
        """ test empty list"""
        res = max_integer([])
        self.assertEqual(res, None)

    # test_04
    def test_max_of_string_list(self):
        """ test list of strings"""
        self.assertEqual(max_integer(["Ab", "ab", "AA"]), "ab")

    # test_05
    def test_max_of_string_int_list(self):
        """test exception can compare int and str"""
        self.assertRaises(TypeError, max_integer, ["A", 100, "a", 66])

    # test_06
    def test_list_of_len_one(self):
        """ test list of len = 1"""
        self.assertEqual(max_integer([101]), 101)
    if __name__ == '__main__':
        unittest.main()
