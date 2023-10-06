#!/usr/bin/python3
"""
this module with one function
"""


def print_square(size):
    """
    print square with symbol #
    Args:
        size: the length of side

    Returns:
        void
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for j in range(size):
        print("#" * size, end="")
        print("")
