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
