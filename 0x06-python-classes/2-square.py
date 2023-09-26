#!/usr/bin/python3
"""Define class Square."""


class Square:
    """implement Square."""
    def __init__(self, size=0):

        """constructor method.

        Args:
            size(int): side len
        """
        if not isintance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
