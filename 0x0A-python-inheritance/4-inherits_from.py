#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
    obj (any): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
