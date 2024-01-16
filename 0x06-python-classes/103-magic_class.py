#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the MagicClass class.
"""

import math


class MagicClass:
    """
    This is the MagicClass class.

    The MagicClass class defines a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        This is the constructor method for the MagicClass class.

        The constructor initializes the radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = radius

    def area(self):
        """
        This is a public instance method for the MagicClass class.

        The area method returns the current circle area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        This is a public instance method for the MagicClass class.

        The circumference method returns the current circle circumference.
        """
        return 2 * math.pi * self.__radius
