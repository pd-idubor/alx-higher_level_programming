#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating  new LockedClass attributes
    except the new attribute called 'first_name'
    """
    __slots__ = ["first_name"]
