#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON retrieval."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student ins
        Args:
            attrs (list): Optional list of strings representing attribute names.
        Returns:
            dict: The dictionary containing the requested attributes.
        """
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return self.__dict__
