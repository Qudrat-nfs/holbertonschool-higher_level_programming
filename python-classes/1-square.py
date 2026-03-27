#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""
class Square:
    """A class that defines a square."""
    def __init__(self, size):
        """Initialize the square with a specific size.
        Args:
            size: The size of the new square.
        """
        self.__size =size
