#!/usr/bin/python3
"""
this module with purpose to test the class Base
"""
import unittest
import models.base as base
from models.base import Base


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
