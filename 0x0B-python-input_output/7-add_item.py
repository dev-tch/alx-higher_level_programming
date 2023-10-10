#!/usr/bin/python3
""" add arguments to file"""
from sys import argv
from os.path import exists


def main():
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file
    filename = "add_item.json"
    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(argv[1:])

    # Save the updated list to "add_item.json"
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
