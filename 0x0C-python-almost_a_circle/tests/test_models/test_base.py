#!/usr/bin/python3
""" Module test for class Base """
import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch, MagicMock


class TestBase(unittest.TestCase):
    """ tests for the class Base methods """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_init_id(self):
        """ Test the __init__ method to create instances with unique ids"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base(40)
        base5 = Base(50)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 40)
        self.assertEqual(base5.id, 50)

    def test_id_assign(self):
        """ create object with and without assigned id"""
        base6 = Base(10)
        base7 = Base()
        base8 = Base(20)
        self.assertEqual(base6.id, 10)
        self.assertEqual(base7.id, 1)
        self.assertEqual(base8.id, 20)

    def test_string_id(self):
        """ Test string id """
        base9 = Base('90')
        self.assertEqual(base9.id, '90')

    def test_multiple_id(self):
        """ Test passing more than one argument to Base init method """
        with self.assertRaises(TypeError):
            base10 = Base(1, 2)

    def test_to_json_string(self):
        """Test if save_to_file saves the JSON representation correctly
        for Base class """

        list_dicts = [
            {'id': 1, 'width': 10, 'height': 5},
            {'id': 2, 'width': 7, 'height': 3}
        ]
        json_str = Base.to_json_string(list_dicts)
        expected_json_str = ('[{"id": 1, "width": 10, "height": 5}, '
                             '{"id": 2, "width": 7, "height": 3}]')
        self.assertEqual(json_str, expected_json_str)

        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_rectangle(self):
        """Test JSON file for Rectangle"""
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_square(self):
        """ Test JSON file for Square """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    @patch('models.base.turtle')
    def test_draw(self, mock_turtle):
        """ Test if draw method opens a window
        and draws the shapes correctly"""

        mock_screen = MagicMock()
        mock_turtle.Screen.return_value = mock_screen
        mock_turtle.Turtle.return_value = mock_turtle

        rect1 = Rectangle(100, 50, 10, 20)
        rect2 = Rectangle(60, 30, 40, 70)
        list_rectangles = [rect1, rect2]

        square1 = Square(70, 5, 15)
        square2 = Square(40, 30, 40)
        list_squares = [square1, square2]

        Base.draw(list_rectangles, list_squares)

        """Ensure that turtle.Screen() and turtle.Turtle() were called"""
        mock_turtle.Screen.assert_called_once()
        mock_turtle.Turtle.assert_called()

        """Ensure that turtle methods for drawing rectangles
        and squares were called"""
        mock_turtle.penup.assert_any_call()
        mock_turtle.goto.assert_any_call(10, 20)
        mock_turtle.pendown.assert_any_call()
        mock_turtle.goto.assert_any_call(10 + 100, 20)
        mock_turtle.goto.assert_any_call(10 + 100, 20 + 50)
        mock_turtle.goto.assert_any_call(10, 20 + 50)
        mock_turtle.goto.assert_any_call(10, 20)

        mock_turtle.penup.assert_any_call()
        mock_turtle.goto.assert_any_call(40, 70)
        mock_turtle.pendown.assert_any_call()
        mock_turtle.goto.assert_any_call(40 + 60, 70)
        mock_turtle.goto.assert_any_call(40 + 60, 70 + 30)
        mock_turtle.goto.assert_any_call(40, 70 + 30)
        mock_turtle.goto.assert_any_call(40, 70)

        mock_turtle.penup.assert_any_call()
        mock_turtle.goto.assert_any_call(5, 15)
        mock_turtle.pendown.assert_any_call()
        mock_turtle.goto.assert_any_call(5 + 70, 15)
        mock_turtle.goto.assert_any_call(5 + 70, 15 + 70)
        mock_turtle.goto.assert_any_call(5, 15 + 70)
        mock_turtle.goto.assert_any_call(5, 15)

        mock_turtle.penup.assert_any_call()
        mock_turtle.goto.assert_any_call(30, 40)
        mock_turtle.pendown.assert_any_call()
        mock_turtle.goto.assert_any_call(30 + 40, 40)
        mock_turtle.goto.assert_any_call(30 + 40, 40 + 40)
        mock_turtle.goto.assert_any_call(30, 40 + 40)
        mock_turtle.goto.assert_any_call(30, 40)

        mock_screen.mainloop.assert_called_once()
