#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    size = 0
    if new_list:
        size = len(my_list)
    if (idx < 0 or idx >= size):
        return (new_list)
    new_list[idx] = element
    return (new_list)
