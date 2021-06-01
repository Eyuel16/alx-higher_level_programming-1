#!/usr/bin/python3
"""
Module 2-append_write
Conatains a function that appends a stting at the end of a
text file
"""


def append_write(filename="", text=""):
    """ appends a text to a given file """
    with open(filename, mode='a', encoding="utf-8") as my_file:
        x = my_file.write(text)
        return x
