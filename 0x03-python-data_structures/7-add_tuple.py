#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        a = 0
        b = 0
        if len(tuple_a) > i:
            a = tuple_a[i]
        if len(tuple_b) > i:
            b = tuple_b[i]
        new_tuple += (a + b,)
    return new_tuple
