#!/usr/bin/python3
"""Adds all command-line arguments to a JSON list file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list (or start empty if file missing)
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add new arguments
my_list.extend(sys.argv[1:])

# Save updated list
save_to_json_file(my_list, filename)
