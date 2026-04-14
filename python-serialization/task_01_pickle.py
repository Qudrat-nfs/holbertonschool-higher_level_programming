#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a binary file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a pickle file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, Exception):
            return None
