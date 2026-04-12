#!/usr/bin/python3
"""Module for appending a string to the end of a text file."""

import json
def save_to_json_file(my_obj, filename):
    """Appends a string to a text file (UTF8) and returns char count."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return json.loads(file.write(my_obj))
