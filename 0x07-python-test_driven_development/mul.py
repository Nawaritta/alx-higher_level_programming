#!/usr/bin/python3
""" Doc """
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print("Failed 1")
m_a = "m_a is a string"
m_b = [[1, 2],[3, 8]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
    print(type(e))

print("Failed 2 ")
m_a = [[1, 2],[3, 8]]
m_b = "m_b is a string"
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
    print(type(e))


print("\n ma = Holberton / mb = [[5, 6], [7, 8]]")


m_a = "Holberton"
m_b = [[5, 6], [7, 8]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
    print(type(e))
