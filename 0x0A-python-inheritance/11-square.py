#!/usr/bin/python3
"""
module with  class Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ implement class Rectangle"""
    def __init__(self, size):
        """constructor method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
