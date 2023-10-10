#!/usr/bin/python3
"""
module with one function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """return  json object from file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return json.load(f)
