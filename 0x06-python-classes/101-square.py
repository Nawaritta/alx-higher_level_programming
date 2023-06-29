#!/usr/bin/python3
"""Python classes."""


class Square:
    """square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of the class square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter of the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter of the position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of the position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """printing the square"""
        if self.__size == 0:
            print()
            return
        print('\n'*self.__position[1], end="")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end="")
            for j in range(self.__size):
                print('#', end="")
            print()

    def __repr__(self):
        string = ""
        """printing the square"""
        if self.__size == 0:
            return string
        print('\n'*self.__position[1], end="")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                string += ' '
            for j in range(self.__size):
                string += '#'
            if i + 1 != self.__size:
                string += '\n'
        return string
