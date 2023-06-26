#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    excep = -1
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            excep += 1
    print()
    return (i - excep)
