#!/usr/bin/python3
"""
This module contains the function text_indentation which adds two new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): The text to be indented.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in ".:?":
            text = text.replace(char, char + "\n\n")
        print("\n".join([line.strip() for line in text.split("\n")]))
