#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
module with  class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """ implement class Rectangle"""

    def __init__(self, width, height):
        """constructor method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
