#!usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max = my_list[0]
        for i in my_list[1:]:
            max = i if i > max else max
        return(max)
