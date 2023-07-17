#!/usr/bin/python3
""" Python almost a circle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle based on the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes the area of the rectangle"""
        return self.width * self.height

    def display(self):
        for yy in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Returns a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """ update the attributes using positional or keyword arguments.
        Positional arguments: updating following the order.
        Keyword arguments: updating a specific given attributes.
        """
        attribute_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                setattr(self, attribute_list[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returs the dictionary representation of Rectangle"""
        attribute_list = ['id', 'width', 'height', 'x', 'y']
        dictionary = {}

        for key in attribute_list:
            dictionary[key] = getattr(self, key)

        return dictionary
