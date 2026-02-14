#!/usr/bin/python3
"""This module defines save_to_json_file function."""

import json


def save_to_json_file(my_obj, filename):
    """This function saves an object to a json file."""
    with open(filename, "w", encoding="utf-8")as f:
        json.dump(my_obj, f)
