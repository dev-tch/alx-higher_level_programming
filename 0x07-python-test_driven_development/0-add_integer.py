#!/usr/bin/python3
"""
this module return sum of two numbers
exception ==> was raised if something is wrong
"""


def add_integer(a, b=98):
    """Returns a + b
    Args:
        a(int): first integer
        b(int): second integer
    Returns:
        int: the sum of a and b
    Raises:
          TypeError: either of argument not int of float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # conversion to int
    int_a = int(a)
    int_b = int(b)

    return int_a + int_b
