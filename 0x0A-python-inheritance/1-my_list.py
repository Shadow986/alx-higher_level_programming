#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list and has a method to
print the list in sorted order.
"""

class MyList(list):
    """
    This class inherits from the built-in list class and includes a method to
    print the list in sorted order.

    Methods:
        print_sorted: Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        This method prints the elements of the list in ascending order. It
        assumes that all elements of the list are integers.
        """
        print(sorted(self))
