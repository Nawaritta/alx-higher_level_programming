#!/usr/bin/python3
"""Python - Inheritance"""


class BaseGeometry:
    """
    Base geo
    Public Methods:
        area(): Raises an exception indicating that
    the area calculation is not implemented.
        integer_validator(name, value): Validates that
    the given value is a positive integer.
    """
    def area(self):
        """
        Raises an exception indicating that
        the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
