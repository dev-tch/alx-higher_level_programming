#!/usr/bin/python3
"""
module with one function read_file
"""


def read_file(filename=""):
    """
    read file and print its lines
    Args:
        filename: name of file to read it
    returns:
        void
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
