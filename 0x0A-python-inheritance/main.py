#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    bg.integer_validator("height", True)
except Exception as e:
    print("err")
    print(e)
    print(type(e))


try:
    bg.integer_validator("distance", True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
