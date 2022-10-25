#!/usr/bin/python3
"""Defines an identity check function"""


def inherits_from(obj, a_class):
    """Checks for instances of a class"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return (True)
    return (False)
