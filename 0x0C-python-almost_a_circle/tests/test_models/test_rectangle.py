#!/usr/bin/python3
"""this module with purpose to test the class TestRectangle"""
import unittest
import models.rectangle as rec_mod
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """
    implement test cases
    """

    def setUp(self):
        """ setup method that run before each test"""
        Base._Base__nb_objects = 0
        self.mock_stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.mock_stdout)
        self.patcher.start()

    def tearDown(self):
        # Restore sys.stdout to its original state after each test
        self.patcher.stop()
        self.mock_stdout.close()

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

    def test_display(self):
        """ test method display"""
        r1 = Rectangle(4, 6)
        r1.display()
        # Get the captured output
        printed_message = self.mock_stdout.getvalue()
        # Assert the printed message matches the expected message
        str1 = "####\n####\n####\n"
        str2 = "####\n####\n####\n"
        msg = f"{str1}{str2}"
        self.assertEqual(printed_message, msg)

    def test_display2(self):
        """ test method display
        """
        r1 = Rectangle(2, 2)
        r1.display()
        # Get the captured output
        printed_message = self.mock_stdout.getvalue()
        # Assert the printed message matches the expected message
        msg = "##\n##\n"
        self.assertEqual(printed_message, msg)

    def test__str__(self):
        """ test method __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        # Get the captured output
        printed_message = self.mock_stdout.getvalue().strip()
        # Assert the printed message matches the expected message
        msg = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(printed_message, msg)

    def test__str__2(self):
        """ test method __str__"""
        r2 = Rectangle(5, 5, 1)
        print(r2)
        # Get the captured output
        printed_message = self.mock_stdout.getvalue().strip()
        # Assert the printed message matches the expected message
        msg = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(printed_message, msg)
