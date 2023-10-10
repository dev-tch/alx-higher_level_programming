#!/usr/bin/python3
"""
module with one function write_file
"""


def write_file(filename="", text=""):
    """
    write text   to file
    Args:
        filename: name of file to write to  it
    returns:
        void
    """
    with open('filename', 'w', encoding="utf-8") as f:
        f.write(text)
