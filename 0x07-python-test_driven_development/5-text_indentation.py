#!/usr/bin/python3
"""
this module with one function text_indentation
"""


def text_indentation(text):
    """
    split text into  lines
    Args:
        text: text of strings
    Returns:
           void
    Raises:
          TypeError: text must be a string
    """
    # text must be a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines = []
    line = []
    seps = "\n.?:"
    for char in text:
        if char in seps:
            if line:
                lines.append("".join(line))
            if char == "\n":
                lines.append("\n")
            else:
                lines.append(char)
                lines.append("\n")
                lines.append("\n")
            line = []
        else:
            line.append(char)
    if line:
        lines.append("".join(line))

    for item in lines:
        if item == "\n":
            print("")
        elif not item.isspace():
            print(item.strip(), end="")
