#!/usr/bin/python
def search_replace(my_list, search, replace):
    return([replace if i is search else i for i in my_list])
