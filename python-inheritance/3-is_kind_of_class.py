#!/usr/bin/python3
"""
Module that checks if an object is exactly an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """
        Returns True if the object is exactly an instance of the
        specified class; otherwise False.
        """
    return isinstance(obj, a_class)
