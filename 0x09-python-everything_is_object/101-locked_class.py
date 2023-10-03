#!/usr/bin/python3
"""declare Locked class"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    except attribute first_name
    """
    __slots__ = ["first_name"]
