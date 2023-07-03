#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """ This class defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new instance of Rectangle
        args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    """sets the height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the ares"""
        return self.__height * self.__width

    def perimeter(self):
        """computes the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for _ in range(self.__height):
            rec_str += '#' * self.__width
            if _ < self.__height - 1:
                rec_str += '\n'
        return rec_str

    def __repr__(self):
        """Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Prints a message when the instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
