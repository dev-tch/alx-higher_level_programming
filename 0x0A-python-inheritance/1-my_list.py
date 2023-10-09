#!/usr/bin/python3
"""
declare class MyList
"""


class MyList(list):
    """implement MyList
    """

    def print_sorted(self):
        self.sort()
        print(self)
