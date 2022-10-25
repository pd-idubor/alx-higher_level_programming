#!/usr/bin/python3
"""Defines an identity check function"""


def is_kind_of_class(obj, a_class):
    """Checks for instances of a class"""
    if (isinstance(obj, a_class)):
        return (True)
    return (False)
