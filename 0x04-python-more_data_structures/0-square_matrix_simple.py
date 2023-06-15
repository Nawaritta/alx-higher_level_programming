#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = []
        for i in matrix:
            lis = []
            for j in i:
                lis += [j*j, ]
            square_matrix += [lis, ]
        return square_matrix
