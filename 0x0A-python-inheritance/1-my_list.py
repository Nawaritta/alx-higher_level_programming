#!/usr/bin/python3
"""Python - Inheritance"""


class MyList(list):
    """
    class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).
        """
        sorted_list = sorted(self)
        print(sorted_list)
