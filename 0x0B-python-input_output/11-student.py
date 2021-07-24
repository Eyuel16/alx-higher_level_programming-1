#!/usr/bin/python3
"""
Method 9-student
Contains a class that defines a student
and a method to retrieve a dictionary representation of the class
"""
class Student():
    """
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description with simple data structure
        """
        return self.__dict__
