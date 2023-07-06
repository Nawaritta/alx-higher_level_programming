#!/usr/bin/python3
"""numpy lazy matrix multiplication"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """ defines a lazy way for multiplying two matrices
    Args:
    m_a: first matrix
    m_b: second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(
            (isinstance(element, int) or isinstance(element, float))
            for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all(
            (isinstance(element, int) or isinstance(element, float))
            for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return numpy.dot(m_a, m_b)
