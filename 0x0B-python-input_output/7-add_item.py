#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then save them to a file.

It uses the function save_to_json_file from 5-save_to_json_file.py
and the function load_from_json_file from 6-load_from_json_file.py

The list must be saved as a JSON representation in a file named add_item.json

If the file doesn't exist, it should be created

You don't need to manage file permissions / exceptions.
"""

from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file


def add_items_to_list(items):
    """
    This function adds all arguments to a Python list, and then save them to a file.

    It uses the function save_to_json_file from 5-save_to_json_file.py
    and the function load_from_json_file from 6-load_from_json_file.py

    The list must be saved as a JSON representation in a file named add_item.json

    If the file doesn't exist, it should be created

    You don't need to manage file permissions / exceptions.

    Args:
        items (list): The list to which the arguments will be added.
    """

    # Get the current list of items from the file
    items_list = load_from_json_file("add_item.json")

    # Add the new items to the list
    items_list.extend(items)

    # Save the new list of items to the file
    save_to_json_file(items_list, "add_item.json")


if __name__ == "__main__":
    # Get the arguments from the command line
    items = sys.argv[1:]

    # Add the items to the list
    add_items_to_list(items)
