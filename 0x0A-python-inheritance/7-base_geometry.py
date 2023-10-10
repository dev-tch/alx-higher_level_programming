#!/usr/bin/python3
"""
module with  class BaseGeometry
"""


class BaseGeometry:
    """implement class BaseGeometry"""

    def area(self):
        """
        method to calculate area of Geometry
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method to validate  integer
        args:
            name(str): name of property
            value(int): value of property
        Returns:
                void
        Raises:
            Exception
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
