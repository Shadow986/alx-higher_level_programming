#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it has a __dict__ attribute.
    Otherwise, raises a TypeError exception with the message "can't add new attribute".
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
