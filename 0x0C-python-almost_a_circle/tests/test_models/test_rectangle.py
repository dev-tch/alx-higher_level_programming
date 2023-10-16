#!/usr/bin/python3
"""this module with purpose to test the class TestRectangle"""
import unittest
import models.rectangle as rec_mod
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    implement test cases
    """

    def setUp(self):
        """ setup method that run before each test"""
        Base._Base__nb_objects = 0

    # test documentation
    def test_doc(self):
        """test doc"""
        self.assertTrue(rec_mod.__doc__)
        self.assertTrue(rec_mod.Rectangle.__doc__)
        self.assertTrue(rec_mod.Rectangle.__init__.__doc__)

    def test_attribute_id(self):
        """ test value of id  attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validate_attributes(self):
        """ test validation attributes"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """ test method area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
