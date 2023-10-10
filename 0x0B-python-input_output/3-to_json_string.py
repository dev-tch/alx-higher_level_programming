#!/usr/bin/python3
"""
module with one function to_json_string
"""
import json


def to_json_string(my_obj):
    """ return the json format of and object"""
    return json.dumps(my_obj)
