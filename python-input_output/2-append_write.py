#!/usr/bin/python3
"""This module defines append_write function."""


def append_write(filename="", text=""):
    """This function appends a text."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
