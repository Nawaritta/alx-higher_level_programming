#!/usr/bin/python3
"""Python - Inheritance"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.
    """
    attributes = []
    methods = []

    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            attributes.append(attr)

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)

    return attributes + methods
