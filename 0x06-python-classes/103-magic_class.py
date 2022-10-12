#!/usr/bin/python3
"""MagicClass definiton from bytecode"""

import math


class MagicClass:
    """Circle"""

    def __init__(self, radius=0):
        """Initialization of MagicClass
            Arg:
                radius (int or float): radius of MagicClass
        """
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self, radius):
        """Returns the area of MagicCircle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self, radius):
        """Returns the circumference of MagicCircle"""
        return (2 * math.pi * self.radius)
