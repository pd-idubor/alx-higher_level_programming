#!/usr/bin/python3
"""Defines a function that confirms identity"""


def is_same_class(obj, a_class):
    """Check identity"""
    if (type(obj) is a_class):
        return (True)
    return (False)
