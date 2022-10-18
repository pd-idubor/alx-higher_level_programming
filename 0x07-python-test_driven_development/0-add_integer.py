#!/usr/bin/python3
"""
    Defines a function that adds two integers
    a: int/float
    b: int/float
"""

def add_integer(a, b=98):
    """
        Returns the sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
