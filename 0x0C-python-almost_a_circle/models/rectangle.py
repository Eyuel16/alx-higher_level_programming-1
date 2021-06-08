#!/usr/bin/python3
"""
Module rectangle
Contains a Rectangle calss
with instance attributes each with its on publec getter andd setter
"""


from models.base import Base


class Rectangle(Base):
    """ a rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instansiates the values """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ returns the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width value """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ returns the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ returns the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the value for x """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ returns the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value for y """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints the rectangle using # """
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="\n")

    def __str__(self):
        """ overdes and prints the given specification """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ assings an argument to each attribute """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.__width = v
                elif k == 2:
                    self.__height = v
                elif k == 3:
                    self.__x = v
                else:
                    self.__y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        dic = {}

        dic["x"] = self.__x
        dic["y"] = self.__y
        dic["id"] = self.id
        dic["height"] = self.__height
        dic["width"] = self.__width
        return dic
