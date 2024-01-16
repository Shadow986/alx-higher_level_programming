#!/usr/bin/python3
"""
This module contains a function that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print a full name.

    Parameters:
    first_name (str): The first name.
    last_name (str): The last name (default "").

    Returns:
    None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
