#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Load the existing list from the file or create a new one
try:
    my_list = load_from_json_file("add_item.json")
except (FileNotFoundError, ValueError):
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(my_list, "add_item.json")
