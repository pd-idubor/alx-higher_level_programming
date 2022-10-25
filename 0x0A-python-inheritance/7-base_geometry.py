#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """A class"""
    def area(self):
        """Raise exceptiin"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
