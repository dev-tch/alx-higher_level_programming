#!/usr/bin/python3
""" module with one class Base"""


class Base:
    """implement class Base"""

    __nb_objects = 0  # class attribute shared by all instances

    def __init__(self, id=None):
        """ constructor class Base"""
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
