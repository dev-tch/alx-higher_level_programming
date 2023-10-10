#!/usr/bin/python3
"""
module with one function from_json_string
"""
import json


def from_json_string(my_str):
    """ return object from string json"""
    return json.loads(my_str)
