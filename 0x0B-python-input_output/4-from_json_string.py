#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        object: A corresponding Python object.
    """
    return json.loads(my_str)
