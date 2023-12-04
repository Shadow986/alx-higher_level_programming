#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    This function takes an object as an argument and returns a list of its
    available attributes and methods.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of the object's attributes and methods.
    """
    return dir(obj)

