#!/usr/bin/python3
"""Module that returns the JSON representation of an object."""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_str)
