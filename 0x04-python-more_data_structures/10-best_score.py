#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = 0
    max_val = None
    max_key = None
    for key, val in a_dictionary.items():
        if (i == 0 or val > max_val):
            max_val = val
            max_key = key
        i += 1
    return (max_key)
