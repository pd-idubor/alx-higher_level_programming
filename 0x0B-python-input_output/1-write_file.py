#!/usr/bin/python3
"""
    Defines a function that writes to a file
"""


def write_file(filename="", text=""):
    """Writes to a text file"""
    with open(filename, 'w', encoding="utf-8") as w:
        return (w.write(text))
