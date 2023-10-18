#!/usr/bin/python3
""" module with one class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """implement class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ format object to string"""
        str1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        return f"{str1} - {self.width}"
