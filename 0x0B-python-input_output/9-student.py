#!/usr/bin/python3
"""A Module of Class Student."""


class Student:
    """A construct of an object Student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.
