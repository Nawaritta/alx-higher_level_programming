#!/usr/bin/python3
""" Doc """

say_my_name = __import__('3-say_my_name').say_my_name

try:
    say_my_name()

except Exception as e:
    print(e)
