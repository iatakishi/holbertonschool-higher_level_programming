#!/usr/bin/python3
"""This module defines student class."""


class Student:
    """This class defines a student object."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and isinstance(attrs, list):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
