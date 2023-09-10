#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if (len1 >= 1):
        sum1 += tuple_a[0]
    if (len1 >= 2):
        sum2 += tuple_a[1]
    if (len2 >= 1):
        sum1 += tuple_b[0]
    if (len2 >= 2):
        sum2 += tuple_b[1]
    new_tuple = (sum1, sum2)
    return (new_tuple)
