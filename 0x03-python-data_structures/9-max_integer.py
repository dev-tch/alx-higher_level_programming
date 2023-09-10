#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max = my_list[0]  # init max to first elem of list
    for item in my_list:
        if (item > max):
            max = item
    return (max)
