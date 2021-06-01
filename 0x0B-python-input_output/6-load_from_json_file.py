#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains a functionthat creates an
Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, encoding="utf-8", mode="r") as my_file:
        return json.load(my_file)
