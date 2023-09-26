#!/usr/bin/python3
"""Define class Square."""


class Square:
    """implement class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """constructor method.

        Args:
            size(int): side len
        """
        self.size = size
        self.position = position

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
        if (self.size == 0):
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """get position.
        Args:
            self(Square): current object
        Returns
              int: poistion
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position property
        Args:
            self(Square): current object
            value: variable to update position
        Returns:
               void: nothing or execption
        """
        test = all((isinstance(i, int) and i >= 0) for i in value)
        if not isinstance(value, tuple) or len(value) != 2 or not test:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
