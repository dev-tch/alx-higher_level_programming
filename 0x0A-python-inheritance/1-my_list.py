#!/usr/bin/python3
"""
declare class MyList
"""


class MyList(list):
    """implement MyList
    """

    def print_sorted(self):
        """
        Args:
            prints the list, but sorted (ascending sort)
        :returns:
            ordered list
        """
        print(sorted(self))
