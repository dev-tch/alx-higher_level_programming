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
        json_str = json.dumps(list_dictionaries)
        return json_str

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(my_list))
