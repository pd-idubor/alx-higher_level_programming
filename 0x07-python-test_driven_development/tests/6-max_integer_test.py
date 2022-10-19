#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer"""

    def test_list(self):
        """Test with a list"""
        self.assertEqual(max_integer([100, 7, 23, 1]), 100)

    def text_max_at_the_end(self):
        """Test with largest int at the end of the list"""
        self.assertEqual(max_integer([43, 47, 50, 54]), 54)

    def test_single_val(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([17]), 17)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_plus_floats(self):
        """Test a list with floats included"""
        floats = [15, 63.7, -7.312, 15.2, 43, 6.0]
        self.assertEqual(max_integer(floats), 63.7)

    def test_no_ints(self):
        """Test with non-numbers included in list of ints"""
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])

    def test_string(self):
        """Test a string"""
        string = "string"
        self.assertEqual(max_integer(string), 't')


if __name__ == '__main__':
    unittest.main()
