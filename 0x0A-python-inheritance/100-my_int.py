#!/usr/bin/python3
"""Defines a class inheriting from int"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Inverts == operator's function to !="""
        return self.real != value

    def __ne__(self, value):
        """Inverts != operator's function to =="""
        return self.real == value
