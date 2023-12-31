#!/usr/bin/python3
"""
script to save and load object Json
"""
import sys


if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file
    file = "add_item.json"
    try:
        new = load_json(file)
    except (ValueError, FileNotFoundError):
        new = []
    for args in sys.argv[1:]:
        new.append(args)
    save_json(new, file)
