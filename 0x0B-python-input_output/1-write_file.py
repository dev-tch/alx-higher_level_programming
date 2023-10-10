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
    nb_written_data = 0
    with open('filename', 'w', encoding="utf-8") as f:
        nb_written_data = f.write(text)
    return nb_written_data
