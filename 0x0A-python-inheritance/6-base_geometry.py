#!/usr/bin/python3
"""Python - Inheritance"""


class BaseGeometry:
    """
    BaseGeo
    Public Methods:
    area(): Raises an exception indicating that
    the area calculation is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")
