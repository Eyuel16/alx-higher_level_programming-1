#!/usr/bin/python3
"""
Method 9-student
Contains a class that defines a student
and a method to retrieve a dictionary representation of the class
"""


class Student:
    """ defines a student based on full name and age """

    def __init__(self, first_name, last_name, age):
        """ instansitiate the values """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return simple dictionaries """
        return self.__dict__
