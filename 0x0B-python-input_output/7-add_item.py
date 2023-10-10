#!/usr/bin/python3
""" add arguments to file"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(argv[1:])

    # Save the updated list to "add_item.json"
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
