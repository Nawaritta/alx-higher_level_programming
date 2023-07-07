#!/usr/bin/python3
""" Devide allthe elements of a matrix by an intger"""


def matrix_divided(matrix, div):
    """
    matrix devider
    args:
    matrix: the matrix of elements to devide by
    div: the devider
    Returns:
    list: A new matrix with all elements divided by div
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf') or div == -float('inf'):
        return [[0.0 for item in row] for row in matrix]

    if matrix == [] or \
       not isinstance(matrix, list) \
       or not all(isinstance(row, list) for row in matrix) \
       or not all(isinstance(element, (int, float))
                  for row in matrix for element in row):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            if item == float('inf') or item == -float('inf') or item != item:
                new_row.append(10.0)
            else:
                new_row.append(item)
        new_matrix.append(new_row)

    new_matrix = [[round(item / div, 2) for item in row]
                  for row in matrix]

    return new_matrix
