#!/usr/bin/python3
"""blueprint for creation object of shape Rectangle."""


class Rectangle:
    """implement properties and methods of class Rectangle."""

    def __init__(self, width=0, height=0):
        """constructor of new object Rectangle
        Args:
            self(Rectangle): current object
            width(int):  short side
            height(int): long side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the attribute width of object Rectangle
        Args:
            self(Rectangel): current object
        Returns:
           int: the short side of rectangle
        """
        return (self.__width)

    @width.setter
def width(self, value):
    """set the attribute width of object Rectangle
    Args:
        self(Rectangel): current object
        value(int): new value of width
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    elif (value < 0):
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """get the attribute height of object Rectangle
    Args:
        self(Rectangel): current object
    Returns:
        int: the long side of rectangle
    """
    return (self.__height)

    @width.setter
    def height(self, value):
        """set the attribute height of object Rectangle
        Args:
            self(Rectangel): current object
            value(int): new value of height
        """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    elif (value < 0):
        raise ValueError("height must be >= 0")
    self.__height = value
