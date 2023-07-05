#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ?
    args:
        text (str): The input text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    found = False
    for c in text:
        if found and c == ' ':
            continue
        found = False
        if c in ['.', '?', ':']:
            print("\n" * 2, end='')
            found = True
        else:
            print(c, end='')
