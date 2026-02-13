#!/usr/bin/python3
"""This module defines the write_file function."""


def write_file(filename="", text=""):
    """This function writes a file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
