#!/usr/bin/python3
"""
Module 1-write_file
Contains a function that writes a string to a
text file
"""


def write_file(filename="", text=""):
    """ writes a text to a given file """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        x = my_file.write(text)
        return x
