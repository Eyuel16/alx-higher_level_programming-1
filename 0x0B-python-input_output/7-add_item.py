#!/usr/bin/python3
"""
Module 7-add_item
ads all arguments to a pythonlist and then save
them to afile
"""

from sys import argv

s = __import__('5-save_to_json_file').save_to_json_file
l = __import__('6-load_from_json_file').load_from_json_file

try:
    files_before = l('add_item.json')
except FileNotFoundError:
    files_before = []

lists = files_before + argv[1:]

s(lists, 'add_item.json')
