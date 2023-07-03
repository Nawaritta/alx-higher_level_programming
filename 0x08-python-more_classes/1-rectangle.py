#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """ This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new instance of Rectangle

        args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the height of the rectangle."""
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
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
