#!/usr/bin/python3
"""This module defines MyList class."""


class MyList(list):
    """This class defines a list object"""

    def print_sorted(self):
        print(sorted(self))
