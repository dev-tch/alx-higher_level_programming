#!/usr/bin/python3
"""blueprint for creation object of shape Rectangle."""


class Rectangle:
    """implement properties and methods of class Rectangle."""

    # common to all objects
    number_of_instances = 0  # public static field
    print_symbol = "#"  # public attribute

    def __init__(self, width=0, height=0):
        """constructor of new object Rectangle
        Args:
            self(Rectangle): current object
            width(int):  short side
            height(int): long side
        Raises:
            TypeError: if width or height are not integer
            ValueError: if width or height are less  than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # increment when create object

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

    @height.setter
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

    def area(self):
        """ return the area of Rectangle"""
        return (self.__width * self.height)

    def perimeter(self):
        """ return the perimeter of Rectangle"""
        if (self.__width == 0 or self.height == 0):
            return (0)
        else:
            return (self.__width + self.height)*2

    def __str__(self):
        """representation string of object Rectangle -for user"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ""
        symbol = str(self.print_symbol)
        for _ in range(self.__height):
            rec_str += symbol * self.__width + "\n"
        return rec_str[:-1]  # Remove the new line

    def __repr__(self):
        """ Representation String for developer
        to create new object (eval function)
        """
        return f"Rectangle({self.width}, {self.__height})"

    def __del__(self):
        """called when an object is garbage collected"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # decrement when object is deleted
