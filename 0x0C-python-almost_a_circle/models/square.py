#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class that represents a square

    Attributes:
        size (int): the size of the square
        x (int): the horizontal position of the square
        y (int): the vertical position of the square
        id (int): the id of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance

        Args:
            size (int): the size of the square
            x (int): the horizontal position of the square
            y (int): the vertical position of the square
            id (int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This is the getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """This is the setter for size."""
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        attributes = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
