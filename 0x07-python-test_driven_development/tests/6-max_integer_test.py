#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_max_at_the_middle(self):
        """Max at the middle"""
        max_list = [9, 20, 74, 8, 13]
        self.assertEqual(max_integer(max_list), 74)

    def test_max_at_begginning(self):
        """Max at beginning"""
        max_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_list), 4)

    def test_max_at_End(self):
        """Max at end"""
        max_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_list), 4)

    def test_one_negative_number(self):
        """one negative number"""
        max_list = [-4, 3, 2, 1]
        self.assertEqual(max_integer(max_list), 3)


    def test_empty_list(self):
        """Test list is empty."""
        max_list = []
        self.assertEqual(max_integer(max_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        max_list = [1]
        self.assertEqual(max_integer(max_list), 1)

if __name__ == '__main__':
    unittest.main()
