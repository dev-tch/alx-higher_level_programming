#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)
    size = 0
    if my_list:
        size = len(my_list)
    if (idx >= size):
        return (my_list)
    del my_list[idx]
    return (my_list)
