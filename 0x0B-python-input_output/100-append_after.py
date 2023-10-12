#!/usr/bin/python3
""" module with one function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after
    each line containing a specific string
    """
    with open(filename, mode='r', encoding='UTF-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='UTF-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(f"{new_string}")
