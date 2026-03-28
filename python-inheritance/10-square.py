#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize the square with a size.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size * self.__size
