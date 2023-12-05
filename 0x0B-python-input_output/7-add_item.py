#!/usr/bin/python3
import sys
import json

# Load the existing list from the file or create a new one
try:
    my_list = json.load(open("add_item.json"))
except (FileNotFoundError, ValueError):
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the list to the file
json.dump(my_list, open("add_item.json", "w"))
