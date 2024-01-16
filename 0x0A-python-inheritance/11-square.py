#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a square with a size attribute"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
