#!/usr/bin/python3
"""Demonstrating Inheritance"""


class MyList(list):
    """Inherits from 'list'"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
