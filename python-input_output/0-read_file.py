#!/usr/bin/python3
"""This module defines read_file function."""


def read_file(filename=""):
    """This function reads a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
