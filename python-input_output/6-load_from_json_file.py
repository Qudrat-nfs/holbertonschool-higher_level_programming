#!/usr/bin/python3
"""Module for saving a Python object to a file in JSON format."""
import json


def load_from_json_file(filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return json.load(file)
