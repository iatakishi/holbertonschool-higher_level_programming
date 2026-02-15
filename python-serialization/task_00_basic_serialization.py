#!/usr/bin/python3
"""This module does serialization."""

import json


def serialize_and_save_to_file(data, filename):
    """This function does serialization."""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    """This function does deserialization."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
