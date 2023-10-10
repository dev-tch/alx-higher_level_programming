#!/usr/bin/python3
"""
module with one function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """save object with format json into file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
