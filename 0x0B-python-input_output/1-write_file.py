#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written

    Args:
        filename (str, optional): the name of the file to write to. Defaults to "".
        text (str, optional): the string to write to the file. Defaults to "".

    Returns:
        int: the number of characters written
    """
    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Write the text to the file and return the number of characters written
        return f.write(text)
