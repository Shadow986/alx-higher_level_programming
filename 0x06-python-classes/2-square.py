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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
