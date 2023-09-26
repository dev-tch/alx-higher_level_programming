#!/usr/bin/python3
"""Define Square class."""


class Square:
    """implement Square class.

    Attributes:
        size(int): side len
    """
    __size
    def __init__(self, size):

        """ constructor method

        Args:
            self(Squre): current object
            size(int): side len
        """
        self.__size = size
