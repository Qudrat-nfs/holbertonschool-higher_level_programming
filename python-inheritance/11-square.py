#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a Square class with a private size attribute.""" 
    def __init__(self, size):
        """
        Initialize the square with a size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square.
        Format: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
