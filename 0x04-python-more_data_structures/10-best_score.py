#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = 0
    max = None
    for val in a_dictionary.values():
        if (i == 0 or val > max):
            max = val
        i += 1
    return (max)
