#!/usr/bin/python3
"""
Module that defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
        An empty class representing base geometry.
    """
    def area(self):
        """Return the area of the geometry."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
