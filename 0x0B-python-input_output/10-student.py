#!/usr/bin/python3
"""
declare class Student
"""


class Student:
    """ implement class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        # init variables
        dict_struct = {}
        is_list = True
        is_item_of_type_str = True

        is_list = isinstance(attrs, list)
        if is_list:
            is_item_of_type_str = all(isinstance(item, str) for item in attrs)
        if not is_list or not is_item_of_type_str:
            return self.__dict__
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    dict_struct[attr] = getattr(self, attr)
        return dict_struct
