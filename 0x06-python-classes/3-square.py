#!/usr/bin/python3
"""Define class Square."""


class Square:
    """implement class Square."""

    def __init__(self, size=0):
        """constructor method.

        Args:
            size(int): side len
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area of Square Shape.

        Args:
            self(Square): current object
        Returns:
               int: the area of Square
        """
        return (self.__size * self.__size)
