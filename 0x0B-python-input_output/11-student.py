#!/usr/bin/python3
"""Python - Input/Output"""


class Student:
    """class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """student constractor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of the Student instance.

        """
        if (isinstance(attrs, list) and all(isinstance(items, str)
                                            for items in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

         Args:
            json (dict): The key/value pairs to replace attributes with.
         """
        for i, j in json.items():
            setattr(self, i, j)
