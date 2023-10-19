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

    @property
    def size(self):
        """getter method for attribute size"""
        return self.width

    @size.setter
    def size(self, size_value):
        """ setter method for attribute size"""
        self.width = size_value
        self.height = size_value

    def update(self, *args, **kwargs):
        """override update method update of class Rectangle"""
        if args:
            # define a list that contains the attributes of object Rectangle
            list_att = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                if i == 4:
                    break
                setattr(self, list_att[i], arg)
                i += 1

        elif kwargs:
            for key, value in kwargs.items():
                returned_attr = getattr(self, key, -1)
                if returned_attr != -1:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        obj_dictionary = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return obj_dictionary
