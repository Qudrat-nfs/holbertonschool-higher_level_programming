#!/usr/bin/python3
""This module defines a Square class with a private size attribute."""
class Square:
    """A class that defines a square."""
    def __init__(self, size = 0):
        """Initialize the square with a specific size."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    self.__size = size
