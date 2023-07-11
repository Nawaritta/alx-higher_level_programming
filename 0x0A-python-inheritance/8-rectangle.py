#!/usr/bin/python3
"""Python - Inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """initializes rectangle"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
