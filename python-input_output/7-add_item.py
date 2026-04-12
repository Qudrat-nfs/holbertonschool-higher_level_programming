#!/usr/bin/python3
"""Script that adds arguments to a Python list, and saves to a file."""
import sys


if __name__ == "__main__":
    save_module = __import__('5-save_to_json_file')
    save_to_json_file = save_module.save_to_json_file

    load_module = __import__('6-load_from_json_file')
    load_from_json_file = load_module.load_from_json_file

    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
