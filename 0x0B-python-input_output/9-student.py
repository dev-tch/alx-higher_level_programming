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

    def to_json(self):
        """that retrieves a dictionary representation of a Student"""
        student_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return student_dict
