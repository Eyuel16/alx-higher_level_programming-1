#!/usr/bin/python3
"""
fins the peak of a list
"""

def find_peak(list_of_integers):
    """ a function to return the first peak found """
    i = 1
    for i in range(len(list_of_integers)):
        if ((list_of_integers[i] >= list_of_integers[i - 1]) and
            (list_of_integers[i] >= list_of_integers[i + 1])):
            return list_of_integers[i]
