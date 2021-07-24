#!/usr/bin/python3
"""
Method 9-student
Contains a class that defines a student
and a method to retrieve a dictionary representation of the class
"""


class Student:
    """Class for student"""
    def __init__(self, first_name, last_name, age):
        """Constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary"""
        return self.__dict__.copy()
