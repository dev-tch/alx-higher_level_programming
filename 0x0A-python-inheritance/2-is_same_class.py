#!/usr/bin/python3
"""
module with one function is_same_class
"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance
    of the specified class otherwise False
    Args:
        obj(Object): python object
        a_class(class): name of class type
    returns:
        True of False
    """
    return type(obj) is a_class
