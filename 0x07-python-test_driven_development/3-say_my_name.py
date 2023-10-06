#!/usr/bin/python3
"""
module with one function to print full name
"""


def say_my_name(first_name, last_name=""):
    """print first and last name with
    Args:
        first_name(str): name of person
        last_name(str): surname of person
    Returns:
        void
    Raises:
        TypeError: first or last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
