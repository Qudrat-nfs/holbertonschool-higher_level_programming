#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it back into a Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
