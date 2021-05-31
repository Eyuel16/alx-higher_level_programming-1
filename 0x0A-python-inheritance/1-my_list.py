#!/usr/bin/python3
"""
Module 1-my_list
Inherits from list
and with funtion print sorted
"""


class MyList(list):
    """
    Module:
    print_sorted(self)
    """

    def print_sorted(self):
        """ lists available attributes """
        print(sorted(self))
