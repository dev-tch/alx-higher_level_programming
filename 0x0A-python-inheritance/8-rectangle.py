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
