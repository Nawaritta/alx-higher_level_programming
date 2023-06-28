#!/usr/bin/python3
"""Python classes"""


class Square:
    """class square."""

    def __init__(self, size=0):
        """Constructor of the class square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter  for the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ equality comparision """
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """less ou equal to"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater or equal to"""
        return self.area() >= other.area()
