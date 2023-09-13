#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = "NOT_FOUND"
    test_val = a_dictionary.get(key, flag)
    if test_val == flag:
        a_dictionary.setdefault(key, value)
    else:
        a_dictionary.update({key: value})
    return (a_dictionary)
