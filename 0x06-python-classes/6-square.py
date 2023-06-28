#!/usr/bin/python3
"""Python classes"""


class Square():
    """square class Coordinates of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Class constructor

        Args:
            size (int): The size of the square (default: 0).
            position (tuple): The position of the square (default: (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")if (type(value) is not int):
        self.__size = value

    @position.setter
    def position(self, value):
        """set position"""
         if not isinstance(value, tuple) or len(value) != 2:
             raise TypeError("position must be a tuple of 2 positive integers")
         if not all(isinstance(coord, int) and coord >= 0 for coord in value):
             raise TypeError("position must be a tuple of 2 positive integers")
         self.__position = value

    def area(self):
        """get area"""
        return self.size ** 2

    def my_print(self):
        """print square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
