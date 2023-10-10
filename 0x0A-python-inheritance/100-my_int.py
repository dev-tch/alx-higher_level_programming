#!/usr/bin/python3
"""
module with  class MyInt
"""


class MyInt(int):
    """implement class MyInt"""

    def __eq__(self, other):
        """ if current == other return False"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ if current == other return True"""
        return super().__eq__(other)
