#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the
json representation of an object
"""

import json


def to_json_string(my_obj):
    """ serializes an object """
    return json.dumps(my_obj)
