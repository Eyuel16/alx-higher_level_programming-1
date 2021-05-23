#!/usr/bin/python3
"""
Module 0-add_integer
Contains on function that returns sum of two integers
Accepts two values (int or float) and cast them to an int
"""


def add_integer(a, b=98):
    """
    Returns a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
