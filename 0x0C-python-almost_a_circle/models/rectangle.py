#!/usr/bin/python3
""" module with one class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """implement class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(id)
        # init attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """"setter for attribute x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for atr y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for atr y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ display rectangle"""
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ format object to string"""
        str1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        return f"{str1} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update method """
        if args:
            # define a list that contains the attributes of object Rectangle
            list_att = ["id", "width", "height", "x", "y"]
            i = 0
            for arg in args:
                if i == 5:
                    break
                setattr(self, list_att[i], arg)
                i += 1

        elif kwargs:
            for key, value in kwargs.items():
                returned_attr = getattr(self, key, -1)
                if returned_attr != -1:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        obj_dictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return obj_dictionary
