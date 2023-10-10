#!/usr/bin/python3
"""
module with one function append_write
"""


def append_write(filename="", text=""):
    """
    append text to the end of file
    """
    nb_appended_data = 0
    with open(filename, 'a', encoding="utf-8") as f:
        nb_appended_data = f.write(text)
    return nb_appended_data
