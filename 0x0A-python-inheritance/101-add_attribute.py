#!/usr/bin/python3
"""
module with  one function
"""


def add_attribute(obj, attr, val_attr):
    """add  new attribute to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val_attr)
