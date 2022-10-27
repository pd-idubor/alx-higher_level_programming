#!/usr/bin/python3
"""
    Defines a function that returns the dict desc with simple data structure
"""


def class_to_json(obj):
    """Returns the dictionary desc for json serialization"""
    return (obj.__dict__)
