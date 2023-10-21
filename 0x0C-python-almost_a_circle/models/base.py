#!/usr/bin/python3
""" module with one class Base"""
import json


class Base:
    """implement class Base"""

    __nb_objects = 0  # class attribute shared by all instances

    def __init__(self, id=None):
        """ constructor class Base"""
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        # exception
        if (not isinstance(list_dictionaries, list) or
                not all(isinstance(x, dict) for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            json_str = "[]"
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            json_str = Base.to_json_string(list_dict)
        with open(file_name, "w") as f:
            f.write(json_str)
