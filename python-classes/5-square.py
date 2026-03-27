#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""
class Square:
    """A class that defines a square."""
    def __init__(self, size = 0):
        """Initialize the square with a specific size."""
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int :
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self) :
            """Return the area of the square."""
            return self.__size * self.__size
    def my_print(self):
        """Print the "#" character of the square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
