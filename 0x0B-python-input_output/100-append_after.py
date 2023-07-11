#!/usr/bin/python3
"""Python - Input/Output"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string

    Args:
    search_string (str):
    new_string (str):
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
