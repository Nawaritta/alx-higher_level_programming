#!/usr/bin/python3
"""Python - Input/Output"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object into its JSON representation as a string.

    Args:
        my_obj (object): The Python object to be serialized.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
