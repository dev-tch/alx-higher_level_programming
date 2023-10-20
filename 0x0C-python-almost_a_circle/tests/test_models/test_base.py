#!/usr/bin/python3
"""
this module with purpose to test the class Base
"""
import unittest
import models.base as base
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch, mock_open
from io import StringIO


class TestBase(unittest.TestCase):
    """
    implement test cases
    """
    # test documentation
    def test_doc(self):
        """test doc"""
        self.assertTrue(base.__doc__)
        self.assertTrue(base.Base.__doc__)
        self.assertTrue(base.Base.__init__.__doc__)

    def test_id(self):
        """ test value of id  attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """test method to_json_string"""
        my_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        list_dict = [my_dict]
        list_dict_str = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        json_dictionary = Base.to_json_string(list_dict)
        self.assertEqual(list_dict_str, json_dictionary)
        self.assertEqual(dict, type(my_dict))
        self.assertEqual(str, type(json_dictionary))
        # test empty list_dict is empty
        self.assertEqual("[]",  Base.to_json_string([]))
        # test list_dict not defined None
        self.assertEqual("[]", Base.to_json_string(None))

    def test_save_to_file(self):
        """test test_save_to_file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        str1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
        str2 = ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        expected = f"{str1}{str2}"
        file_name = 'Rectangle.json'
        with patch('builtins.open', mock_open()) as mock_file:
            Rectangle.save_to_file(Rectangle, [r1, r2])
            mock_file.assert_called_with(file_name, 'w', encoding='UTF-8')
            mock_file().write.assert_called_with(expected)
