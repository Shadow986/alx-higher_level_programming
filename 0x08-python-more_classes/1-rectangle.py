#!/usr/bin/python3
"""This module contains a class Rectangle that defines a rectangle."""

class Rectangle:
    """This class defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """This method initializes a rectangle instance with optional width and height parameters."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This property returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter method sets the width of the rectangle to a positive integer value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This property returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter method sets the height of the rectangle to a positive integer value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
