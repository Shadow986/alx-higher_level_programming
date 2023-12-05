#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
        filename (str): the name of the file to be modified.
        search_string (str): the string to be searched in each line.
        new_string (str): the string to be inserted after the search string.

    Returns:
        None
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + "\n")
