#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Function to add two numbers.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number (default 98).

    Returns:
    int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
