#!/usr/bin/python3

""" Python classes"""

import math


class MagicClass:
    """
    A magical class that represents a circle and its characteristics.
    """

    def __init__(self, radius):
        """
        Constructor of the MagicClass

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.
        """
        return 2 * math.pi * self.__radius
