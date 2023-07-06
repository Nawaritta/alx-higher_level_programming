#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer


try:
    print(add_integer(float('nan')))
except Exception as e:
    print(e)
try:
    print(add_integer(float('nan'), 5))
except Exception as e:
    print(e)
    print("Exception type:", type(e).__name__)
