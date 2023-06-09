#!/usr/bin/python3
"""Python - Input/Output"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
