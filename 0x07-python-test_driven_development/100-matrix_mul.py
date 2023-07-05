#!/usr/bin/python3
"""matrix multiplication"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices.

    args:
        m_a(list of lists of float or int): first matrix
        m_b(list of lists of float or int): The second matrix.
    Returns:
       The matrix representing the multiplication of the m_a by m_b.
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


    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")


    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invers_m_b = []
    for c in range(len(m_b[0])):
        invers_col = []
        for r in range(len(m_b)):
            invers_col.append(m_b[r][c])
        invers_m_b.append(invers_col)

    mul_matrix = []
    for row in m_a:
        invers_row = []
        for col in invers_m_b:
            x = 0
            for i in range(len(invers_m_b[0])):
                x += row[i] * col[i]
            invers_row.append(x)
        mul_matrix.append(invers_row)

    return mul_matrix
