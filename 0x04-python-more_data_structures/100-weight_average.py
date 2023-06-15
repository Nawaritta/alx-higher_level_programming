#!/usr/bin/python3
def weight_average(my_list=[]):
   A = 0
   B = 1
   if my_list:
       B = 0
       for element in my_list:
           A += element[0] * element[1]
           B += element[1]
   return (A / B)
