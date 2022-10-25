#!/usr/bin/python3
"""Defines a function that returns a list object"""


def lookup(obj):
    """Returns list of available attributes of an object"""
    return (dir(obj))
