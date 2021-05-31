#!/usr/bin/python3
"""
Moduele 5-base_geometry.py
Empty BaseGeometry
Class
"""
class BaseGeometry:
    """ Base Geometry """
    def area(self):
        """ Calculates the area of the geometry """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates input """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
