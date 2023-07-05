#!/usr/bin/python3
""" This function adds two integrs"""


def add_integer(a, b=98):
    """
    args:
    param a: must be integer or float
    param b:  (Default value = 98)

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a) + int(b)
