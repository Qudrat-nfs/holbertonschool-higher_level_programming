#!/usr/bin/python3
"""Module for reading a text file and printing it to stdout."""


def write_file(filename="", text=""):
    """Reads a text file in UTF-8 format and prints it to stdout."""
    with open(filename, mode="w", encoding="utf-8") as file:
        print(file.write(), end="")
