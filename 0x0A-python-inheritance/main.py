#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    bg.integer_validator("height", True)
    print("no")
except Exception as e:
    print("err")
    print(e)
    print(type(e))
