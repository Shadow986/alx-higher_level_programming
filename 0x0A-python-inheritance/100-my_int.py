#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """A class for integers that inverts the == and != operators"""

    def __eq__(self, other):
        """Method that inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Method that inverts the != operator"""
        return super().__eq__(other)
