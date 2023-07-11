#!/usr/bin/python3
"""Python - Input/Output"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Args:
        obj (object): An instance of a class.
    """
    result = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
        elif hasattr(value, "__dict__"):
            result[attr] = class_to_json(value)
    return result
