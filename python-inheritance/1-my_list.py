#!/usr/bin/python3
"""class Mylist inherits list"""
class Mylist(list):
    """this function sorted int list"""
    def print_sorted(self):
        print(sorted(self))
