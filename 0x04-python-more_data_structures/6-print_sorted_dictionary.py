#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = list(a_dictionary.keys())
    list_keys.sort()
    for key in list_keys:
        print("{:s}: ".format(key), end="")
        print(a_dictionary.get(key))
