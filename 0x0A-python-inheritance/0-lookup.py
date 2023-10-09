#!/usr/bin/python3
"""
 module with one function lookup(obj)
"""


def lookup(obj):
    """
    function to return all available properties and methods of and object
    Args:
        obj(Object): python object
    returns:
        list of properties and methods of object
    """
    return dir(obj)
