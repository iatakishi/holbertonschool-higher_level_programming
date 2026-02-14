#!/usr/bin/python3
"""This module defines load_from_json_file function."""

import json


def load_from_json_file(filename):
    """This function loads from a json file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
