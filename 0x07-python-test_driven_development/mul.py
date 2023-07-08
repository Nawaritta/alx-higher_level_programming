#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul


try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))

except Exception as e:
    print(e)
    print(type(e))




try:
    print(matrix_mul([[1, 2], [3, 4]]))

except Exception as e:
    print(e)
    print(type(e))

try:
    print(matrix_mul())

except Exception as e:
    print(e)
    print(type(e))
