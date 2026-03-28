#!/usr/bin/python3
#!/usr/bin/python3
"""
Module that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
