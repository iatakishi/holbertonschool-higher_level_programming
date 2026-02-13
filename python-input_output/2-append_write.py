#!/usr/bin/python3
"""This module defines append_write function."""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
