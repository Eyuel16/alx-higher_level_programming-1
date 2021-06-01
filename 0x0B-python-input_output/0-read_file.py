#!/usr/bin/python3
"""
Module 0-read_file
Contains a function that reads a text file (UTF-8)
doesn't specifiy permission
"""


def read_file(filename=""):
    """ reads a file """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read())
