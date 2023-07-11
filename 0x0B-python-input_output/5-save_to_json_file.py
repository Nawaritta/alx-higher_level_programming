#!/usr/bin/python3
"""Python - Input/Output"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write a function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (object): The Python object to be serialized.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
