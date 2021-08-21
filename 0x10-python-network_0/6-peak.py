#!/usr/bin/python3
"""
fins the peak of a list
"""

def find_peak(list_of_integers):
    """ a function to return the first peak found """
    for i in range(1, len(list_of_integers)):
        if i + 1 >= len(list_of_integers):
            return None
        if ((list_of_integers[i] >= list_of_integers[i - 1]) and
            (list_of_integers[i] >= list_of_integers[i + 1])):
            return list_of_integers[i]
