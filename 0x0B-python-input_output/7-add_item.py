#!/usr/bin/python3
""" add arguments to file"""
from sys import argv
import json


def load_from_json_file(file):
    """return  json object from file"""
    with open(file) as f:
        return json.load(f)


def save_to_json_file(my_obj, file):
    """save object with format json into file"""
    with open(file, 'w') as f:
        json.dump(my_obj, f)


def main():
    filename = "add_item.json"
    try:
        content = load_from_json_file(filename)
    except FileNotFoundError:
        content = []

    for i in range(1, len(argv)):
        content.append(argv[i])
    save_to_json_file(content, filename)


if __name__ == "__main__":
    main()
