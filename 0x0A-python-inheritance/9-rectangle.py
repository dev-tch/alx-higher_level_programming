#!/usr/bin/python3
"""
module with  class BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ implement class Rectangle"""
    def __init__(self, width, height):
        """constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        method to calculate area of Geometry
        Returns:
            area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """object string representation"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
