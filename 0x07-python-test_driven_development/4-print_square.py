#!/usr/bin/python3
"""
    Defines a function that lrints a square
"""


def print_square(size):
    """Prints a square with '#'"""

    if isinstance(size, float):
        if (size < 0):
            raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("{}".format("#" * size))
