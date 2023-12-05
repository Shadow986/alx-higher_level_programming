#!/usr/bin/python3
"""
This module defines a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): the name of the file to read. Defaults to "".

    Returns:
        None
    """
    # Use the with statement to open the file and ensure it is closed
    with open(filename, "r", encoding="utf-8") as f:
        # Use the read method to read the entire file content
        content = f.read()
        # Print the content to stdout
        print(content)
