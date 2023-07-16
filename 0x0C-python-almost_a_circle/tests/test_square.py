#!/usr/bin/python3
""" Module for test Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        """ Set up a new Square instance for each test """
        self.square = Square(5, 2, 3, 1)

    def test_area(self):
        self.assertEqual(self.square.area(), 25)

    def test_display(self):
        """Redirecting stdout to a variable for testing display output"""
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        self.square.display()
        expected_output = "\n" * 3 + "  #####\n" * 5
        self.assertEqual(captured_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__

    def test_str(self):
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected_str)

    def test_update(self):
        self.square.update(4, 8)
        expected_str = "[Square] (4) 2/3 - 8"
        self.assertEqual(str(self.square), expected_str)

        self.square.update(size=15, x=7, id=8)
        expected_str = "[Square] (8) 7/3 - 15"
        self.assertEqual(str(self.square), expected_str)

    def test_to_dictionary(self):
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_invalid_size(self):
        with self.assertRaises(ValueError) as context:
            self.square.size = -5
        self.assertEqual(str(context.exception), "size must be > 0")

        with self.assertRaises(TypeError) as context:
            self.square.size = "invalid_size"
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as context:
            self.square.x = -2
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            self.square.x = "invalid_x"
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as context:
            self.square.y = -3
        self.assertEqual(str(context.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as context:
            self.square.y = "invalid_y"
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_invalid_id(self):
        with self.assertRaises(TypeError) as context:
            self.square.id = "invalid_id"
        self.assertEqual(str(context.exception), "id must be an integer")


if __name__ == "__main__":
    unittest.main()
