#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

    Parameters:
    obj (any): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if obj is an instance or subclass instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
