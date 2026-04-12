#!/usr/bin/python3
"""Module for saving a Python object to a file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
