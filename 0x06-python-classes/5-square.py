#!/usr/bin/python3
"""Define class Square."""


class Square:
    """implement class Square."""

    def __init__(self, size=0):
        """constructor method.

        Args:
            size(int): side len
        """
        self.size = size

    def area(self):
        """calculate area of Square Shape.

        Args:
            self(Square): current object
        Returns:
               int: the area of Square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """get size attribute.

        Args:
           self(Square): current object
        Returns:
               int: side len
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size attribute.

        Args:
            self(square): current object
            value(int): value to update __size
        Returns:
               void: nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
        if (self.size == 0):
            print()
