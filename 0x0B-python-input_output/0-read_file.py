#!/usr/bin/python3
"""
    Defines a function that reads a text file
"""


def read_file(filename=""):
    """Reads a text file"""
    with open('my_file_0.txt', encoding="utf-8") as r:
        read_d = r.read()
        print(read_d, end="")
