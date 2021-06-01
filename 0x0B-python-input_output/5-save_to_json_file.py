#!/usr/bin/python3
"""
Module 5-save-to_json_file
Contains a function that writes an Object to
a text file using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
