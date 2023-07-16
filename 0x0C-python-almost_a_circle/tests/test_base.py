import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        """Clear any existing files before each test"""
        for cls in [Base, Rectangle, Square]:
            filename = cls.__name__ + ".json"
            if os.path.exists(filename):
                os.remove(filename)
            filename_csv = cls.__name__ + ".csv"
            if os.path.exists(filename_csv):
                os.remove(filename_csv)

    def test_init(self):
        """ Test the __init__ method to create instances with unique ids"""
        base1 = Base()
        base2 = Base()
        base3 = Base(10)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 10)

    def test_to_json_string(self):
        """Test if to_json_string returns the correct JSON representation"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        list_rectangles = [rect1, rect2]

        expected_result = '[{"x": 0, "y": 0, "id": 1, "width": 10, "height": 5}, {"x": 0, "y": 0, "id": 2, "width": 7, "height": 3}]'
        self.assertEqual(Base.to_json_string([rect1.to_dictionary(), rect2.to_dictionary()]), expected_result)

    def test_save_to_file(self):
        """Test if save_to_file saves the JSON representation correctly"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        list_rectangles = [rect1, rect2]
        Base.save_to_file(list_rectangles)

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

    def test_load_from_file(self):
        """Test if load_from_file returns the correct list of instances"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        list_rectangles = [rect1, rect2]
        Base.save_to_file(list_rectangles)

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 5)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[1].width, 7)
        self.assertEqual(instances[1].height, 3)

    def test_save_to_file_csv(self):
        """ Test if save_to_file_csv saves the CSV representation correctly"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        list_rectangles = [rect1, rect2]
        Base.save_to_file_csv(list_rectangles)

        filename = "Rectangle.csv"
        self.assertTrue(os.path.exists(filename))

    def test_load_from_file_csv(self):
        """Test if load_from_file_csv returns the correct list of instances"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(7, 3)
        list_rectangles = [rect1, rect2]
        Base.save_to_file_csv(list_rectangles)

        instances = Base.load_from_file_csv()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 5)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[1].width, 7)
        self.assertEqual(instances[1].height, 3)


    def test_from_json_string(self):
        """Test if from_json_string returns the correct list of dictionaries"""
        json_str = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 7, "height": 3}]'
        expected_result = [{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 7, "height": 3}]
        self.assertEqual(Base.from_json_string(json_str), expected_result)

    def test_create(self):
        """Test if create returns the correct instance with attributes set"""
        rect_dict = {"id": 1, "width": 10, "height": 5}

    @patch('models.base.turtle')
    def test_draw(self, mock_turtle):
        """ Test if draw method opens a window and draws the shapes correctly"""

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

        """Ensure that turtle methods for drawing rectangles and squares were called"""
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

if __name__ == "__main__":
    unittest.main()
