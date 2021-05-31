#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
and with funtion print sorted
"""


class MyList(list):
    """ Inherits from list

    Module:
    print_sorted(self)
    """

    def print_sorted(self):
        """ lists available attributes """
        print(sorted(self))
