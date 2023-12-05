#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (object): an instance of a Class

    Returns:
        dict: a dictionary containing all attributes of obj that are
        serializable
    """
    return obj.__dict__
