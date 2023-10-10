#!/usr/bin/python3
import json
"""
module with one function to_json_string
"""


def to_json_string(my_obj):
    """ return the json format of and object"""
    return json.dumps(my_obj)
