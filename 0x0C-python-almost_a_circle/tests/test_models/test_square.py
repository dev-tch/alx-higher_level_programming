#!/usr/bin/python3
"""this module with purpose to test the class Square"""
import unittest
import models.square as sq_mod
from models.square import Square
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestSquare(unittest.TestCase):
    """
    implement test cases
    """
    s1 = None
    s2 = None
    s3 = None

    def setUp(self):
        """ setup method that run before each test"""
        Base._Base__nb_objects = 0
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.mock_stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.mock_stdout)
        self.patcher.start()

    def tearDown(self):
        # Restore sys.stdout to its original state after each test
        del self.s1
        del self.s2
        del self.s3
        self.patcher.stop()
        self.mock_stdout.close()

    # test documentation
    def test_doc(self):
        """test doc"""
        self.assertTrue(sq_mod.__doc__)
        self.assertTrue(sq_mod.Square.__doc__)
        self.assertTrue(sq_mod.Square.__init__.__doc__)
        self.assertTrue(sq_mod.Square.__str__.__doc__)

    def test___str___(self):
        """ test __str__"""
        print(self.s1)
        print(self.s2)
        print(self.s3)
        my_lst = list()
        my_lst.append("[Square] (1) 0/0 - 5\n")
        my_lst.append("[Square] (2) 2/0 - 2\n")
        my_lst.append("[Square] (3) 1/3 - 3\n")
        res = self.mock_stdout.getvalue()
        expected = "".join(my_lst)
        self.assertEqual(res, expected)

    def test_area(self):
        """test area"""
        print(self.s1.area())
        print(self.s2.area())
        print(self.s3.area())
        res = self.mock_stdout.getvalue()
        expected = "25\n4\n9\n"
        self.assertEqual(res, expected)

    def test__display(self):
        """test display method"""
        my_lst = ["#####\n",
                  "#####\n",
                  "#####\n",
                  "#####\n",
                  "#####\n",
                  "  ##\n",
                  "  ##\n",
                  "\n\n\n",
                  " ###\n",
                  " ###\n",
                  " ###\n"]
        self.s1.display()
        self.s2.display()
        self.s3.display()
        res = self.mock_stdout.getvalue()
        expected = "".join(my_lst)
        self.assertEqual(res, expected)

    def test_get_set_size(self):
        """ method to test getter and setter of attribute size"""
        Base._Base__nb_objects = 0
        sq_obj = Square(5)
        print(sq_obj)
        print(sq_obj.size)
        sq_obj.size = 10
        print(sq_obj)
        my_lst = ["[Square] (1) 0/0 - 5\n",
                  "5\n",
                  "[Square] (1) 0/0 - 10\n"
                  ]
        res = self.mock_stdout.getvalue()
        expected = "".join(my_lst)
        self.assertEqual(res, expected)
        with self.assertRaises(TypeError):
            sq_obj.size = "9"

    def test_update(self):
        """test update method"""
        Base._Base__nb_objects = 0
        sq_obj = Square(5)
        print(sq_obj)
        sq_obj.update(10)
        print(sq_obj)
        sq_obj.update(1, 2)
        print(sq_obj)
        sq_obj.update(1, 2, 3)
        print(sq_obj)
        sq_obj.update(1, 2, 3, 4)
        print(sq_obj)
        sq_obj.update(x=12)
        print(sq_obj)
        sq_obj.update(size=7, y=1)
        print(sq_obj)
        sq_obj.update(size=7, id=89, y=1)
        print(sq_obj)
        my_lst = ["[Square] (1) 0/0 - 5\n",
                  "[Square] (10) 0/0 - 5\n",
                  "[Square] (1) 0/0 - 2\n",
                  "[Square] (1) 3/0 - 2\n",
                  "[Square] (1) 3/4 - 2\n",
                  "[Square] (1) 12/4 - 2\n",
                  "[Square] (1) 12/1 - 7\n",
                  "[Square] (89) 12/1 - 7\n"
                  ]
        res = self.mock_stdout.getvalue()
        expected = "".join(my_lst)
        self.assertEqual(res, expected)

    def test_to_dictionary(self):
        """test method to_dictionary"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        print(s1)
        s1_dictionary = s1.to_dictionary()
        print(s1_dictionary)
        print(type(s1_dictionary))
        s2 = Square(1, 1)
        print(s2)
        s2.update(**s1_dictionary)
        print(s2)
        print(s1 == s2)
        my_lst = ["[Square] (1) 2/1 - 10\n",
                  "{'id': 1, 'size': 10, 'x': 2, 'y': 1}\n",
                  "<class 'dict'>\n",
                  "[Square] (2) 1/0 - 1\n",
                  "[Square] (1) 2/1 - 10\n",
                  "False\n"
                  ]
        res = self.mock_stdout.getvalue()
        expected = "".join(my_lst)
        self.assertEqual(res, expected)
