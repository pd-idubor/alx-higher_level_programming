#!/usr/bin/python3
"""
    Defines a function that appends data to a file
"""


def append_write(filename="", text=""):
    """Appends a string to a textfile"""
    with open(filename, 'a', encoding="utf-8") as a:
        return (a.write(text))
