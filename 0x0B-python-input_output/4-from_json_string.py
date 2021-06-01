#!/usr/bin/python3
"""
MOdule 4-from_josn_string
Contains a function that rerutnrs an object
(python data structure from a JSON string
"""

import json


def from_json_string(my_str):
    """ deserializes a json representation """
    return json.loads(my_str)
