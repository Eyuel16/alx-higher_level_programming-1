#!/usr/bin/python3
"""
Module 12-pascal_triangle
Contains a function that returns a list of
integers representing the pascal's triangle of n
"""


def pascal_triangle(n):
    """ prints a pascal triangle with size n """
    pascal_list = [1]
    for i in range(n):
        pascal_list[i] = 1
        for j in range(n):
            pascal_list[i][j] = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
    print (pascal_list)
    return pascal_list
