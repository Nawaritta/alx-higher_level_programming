#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Returns the first peak if it exists
    """
    if not list_of_integers or len(list_of_integers) == 0:
        return None
    i = 0
    up = 0
    while i < len(list_of_integers):
        peak = list_of_integers[i]
        if len(list_of_integers) > i+1:
            if list_of_integers[i+1] >= list_of_integers[i]:
                up = 1
                i += 1
                peak = list_of_integers[i]
            else:
                i += 1
            if up and (i+1 < len(list_of_integers)):
                if list_of_integers[i+1] < list_of_integers[i]:
                    return list_of_integers[i]
        i += 1

    return peak
