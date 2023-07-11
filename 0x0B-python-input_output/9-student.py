#!/usr/bin/python3
"""Python - Input/Output"""


class Student:
    """class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """student constractor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of the Student instance.

        """
        return self.__dict__
