#!/usr/bin/python3
""" Python almost a circle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square: This class inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes using positional or keyword arguments.
        Positional arguments: updating following the order.
        Keyword arguments: updating specific given attributes.
        """
        attribute_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        attribute_list = ['id', 'size', 'x', 'y']
        dictionary = {}
        for key in attribute_list:
            dictionary[key] = getattr(self, key)
        return dictionary
