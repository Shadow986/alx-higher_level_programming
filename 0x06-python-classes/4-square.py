#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the Square class.
"""


class Square:
    """
    This is the Square class.

    The Square class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for the Square class.

        The constructor initializes the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter method for the Square class.

        The size method retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for the Square class.

        The size method sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This is a public instance method for the Square class.

        The area method returns the current square area.
        """
        return self.__size ** 2
