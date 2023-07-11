#!/usr/bin/python3
"""Python - Input/Output"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle for a given integer n.

    Args:
        n (int): The number of lines in Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        line = [1]
        prev_line = triangle[i-1]
        for j in range(1, i):
            line.append(prev_line[j-1] + prev_line[j])

        line.append(1)
        triangle.append(line)

    return triangle
