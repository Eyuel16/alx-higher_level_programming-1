#!/usr/bin/python3

"""
Module base
Contains Class Base
with objectect counter
"""

import json


class Base:
    """ a Base class for other geometry classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the value """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        dic = []

        if list_objs is not None:
            for obj in list_objs:
                dic.append(cls.to_dictionary(obj))

        myfile = cls.__name__ + ".json"

        with open(myfile, "w") as my_file:
            my_file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """
retruns the list of the JSON string representation of json_string
        """
        if json_string is None:
            json_string = "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        listObjects = []
        try:
            with open(filename, "r") as f:
                strinstances = f.read()
                listOfInstances = cls.from_json_string(strinstances)
            for i, dic in enumerate(listOfInstances):
                listObjects.append(cls.create(**listOfInstances[i]))
        except BaseException:
            pass
        return listObjects
