#!/usr/bin/python3
"""numpy lazy matrix multiplication"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """ defines a lazy way for multiplying two matrices
    Args:
    m_a: first matrix
    m_b: second matrix
    """
    return numpy.matmul(m_a, m_b)
