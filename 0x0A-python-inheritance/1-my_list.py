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
        s = self[:]
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] <= s[j]:
                    s[i], s[j] = s[j], s[i]
        print (s)
