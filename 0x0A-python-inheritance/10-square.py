#!/usr/bin/python3
"""Python - Inheritance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the specified size.

        Args:
        size (int): The size of the square.
        """
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Returns a string representation of the square.
        """
        return self.__str__()

    def print(self):
        """
        Prints the string representation of the square.
        """
        print(self.__str__())
