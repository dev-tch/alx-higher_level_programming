#!/usr/bin/python3
"""
module with one function inherits_from
"""


def inherits_from(obj, a_class):
    """
    return True if Object instance of subclass
    Args:
       obj(Object): python object
       a_class(class): name of class type
    returns:
       True of False
   """
    return type(obj) != a_class and issubclass(type(obj), a_class)
