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
        with open(file_name, "w", encoding="UTF-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        shape_obj = None
        if cls.__name__ == "Rectangle":
            shape_obj = cls(2, 1)
        elif cls.__name__ == "Square":
            shape_obj = cls(2)
        shape_obj.update(**dictionary)
        return shape_obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r') as file:
                json_obj = json.load(file)
                instances = []
                for item in json_obj:
                    instance = cls.create(**item)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
