#!/usr/bin/python3
"""
module to compute peak of list int
"""


def find_peak(list_of_integers):
    """return peak of list"""
    if not list_of_integers or not isinstance(list_of_integers, list):
        return None
    size = len(list_of_integers)
    return find_peak_recursive(list_of_integers, 0, size - 1)


def find_peak_recursive(lst, start, end):
    """ helper function to get peak inside interval"""
    if start == end:
        return lst[start]
    m = int((start + end) // 2)
    if lst[m] > lst[m + 1] and lst[m] > lst[m - 1]:
        return lst[m]
    if lst[m + 1] > lst[m]:
        return find_peak_recursive(lst, m + 1, end)
    else:
        return find_peak_recursive(lst, 0, m - 1)
