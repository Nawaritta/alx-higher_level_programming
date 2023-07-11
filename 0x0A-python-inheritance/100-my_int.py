#!/usr/bin/python3

"""python-inheritance."""


class MyInt(int):
    """Rebel int that inverts operators == and !="""

    def __eq__(self, other):
        """inverts the behavior of == opeartor."""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts the behavior of != operator."""
        return super().__eq__(other)
