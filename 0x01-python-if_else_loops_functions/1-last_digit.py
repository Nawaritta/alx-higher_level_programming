#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print(f"Last digit of {number} is {ld} and is ", end="")

if ld < 6 and ld != 0:
    print("less than 6 and not 0")
elif ld == 0:
    print("0")
else:
    print("greater than 5")
