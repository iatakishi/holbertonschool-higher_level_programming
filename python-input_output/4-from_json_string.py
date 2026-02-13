#!/usr/bin/python3
"""This module defines from_json_string function."""

import json


def from_json_string(my_obj):
    """This function converts json to Python data structures."""
    return json.loads(my_obj)
