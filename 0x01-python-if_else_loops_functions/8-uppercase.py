#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = 0
        if(ord(c) >= 97 and ord(c) <= 122):
            upper = 32
            print(f"{chr(ord(c) - upper)}", end="")
            print()
