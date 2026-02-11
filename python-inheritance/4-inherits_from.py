#!/usr/bin/python3
"""This module define the function inherits_from."""


def inherits_from(obj, a_class):
    """This function checks if an object is inherited from a class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
