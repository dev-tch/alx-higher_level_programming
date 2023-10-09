#!/usr/bin/python3
"""
module with one function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    return True if Object is kind a_class
    Args:
        obj(Object): python object
        a_class(class): name of class type
    returns:
        True of False
    """
    return isinstance(obj, a_class)
