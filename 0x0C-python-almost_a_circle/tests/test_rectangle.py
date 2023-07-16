import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """ Set up a new Rectangle instance for each test """
        self.rectangle = Rectangle(10, 5, 2, 3, 1)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    def test_display(self):
        """ Redirecting stdout to a variable for testing display output"""
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        self.rectangle.display()
        expected_output = "\n" * 3 + "  ##########\n" * 5
        self.assertEqual(captured_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__

    def test_str(self):
        expected_str = "[Rectangle] (1) 2/3 - 10/5"
        self.assertEqual(str(self.rectangle), expected_str)

    def test_update(self):
        self.rectangle.update(4, 20)
        expected_str = "[Rectangle] (4) 2/3 - 20/5"
        self.assertEqual(str(self.rectangle), expected_str)

        self.rectangle.update(height=15, x=7, id=8)
        expected_str = "[Rectangle] (8) 7/3 - 20/15"
        self.assertEqual(str(self.rectangle), expected_str)

    def test_to_dictionary(self):
        expected_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            self.rectangle.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(TypeError) as context:
            self.rectangle.width = "invalid_width"
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_height(self):
        with self.assertRaises(ValueError) as context:
            self.rectangle.height = -5
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(TypeError) as context:
            self.rectangle.height = "invalid_height"
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as context:
            self.rectangle.x = -2
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            self.rectangle.x = "invalid_x"
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as context:
            self.rectangle.y = -3
        self.assertEqual(str(context.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as context:
            self.rectangle.y = "invalid_y"
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_invalid_id(self):
        with self.assertRaises(TypeError) as context:
            self.rectangle.id = "invalid_id"
        self.assertEqual(str(context.exception), "id must be an integer")


if __name__ == "__main__":
    unittest.main()
