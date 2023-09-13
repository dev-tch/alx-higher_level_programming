#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new_list.sort()
    prev = -1
    sum = 0
    for item in new_list:
        if (prev != item):
            sum = sum + item
        prev = item
    return (sum)
