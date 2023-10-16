import unittest
import models.base as base
from models.base import Base
"""
this module with purpose to test the class Base
"""


class TestMaxInteger(unittest.TestCase):
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
