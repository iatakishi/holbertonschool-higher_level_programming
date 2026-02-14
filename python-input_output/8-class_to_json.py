#!/usr/bin/python3
"""Returns dictionary description of object for JSON serialization."""


def class_to_json(obj):
    return obj.__dict__
