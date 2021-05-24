#!/usr/bin/python3
"""
Module 1-rectangle
defines a rectangle
sets and retirieves width and height
"""


class Rectangle:
    """
    defines a rectangle

    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    
    def __init__(self, width=0, height=0):
        """ initialize rectangle """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """ width Getter """
        return self.__width
    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueErro("width must be >= 0")
        else:
            self.__width = value
    @property
    def	height(self):
        """ height getter """
        return self.__height
    @height.setter
    def	height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueErro("width must be >= 0")
        else:
            self.__height = value
