#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8) and returns the number of characters added.
    If the file doesn’t exist, it should be created.
    The function uses the with statement to ensure proper file handling.
    """
    # open the file in append mode
    with open(filename, mode="a", encoding="utf-8") as f:
        # write the text to the file
        f.write(text)
        # return the number of characters added
        return len(text)
