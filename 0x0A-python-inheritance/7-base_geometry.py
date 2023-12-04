#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A class for geometric shapes"""

    def area(self):
        """Method that raises an exception for unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates an integer value

        Args:
            name (str): the name of the value
            value (int): the value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
