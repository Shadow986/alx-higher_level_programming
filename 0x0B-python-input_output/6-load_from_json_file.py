#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object corresponding to the JSON data.
    """
    with open(filename, 'r') as f:
        return json.load(f)
