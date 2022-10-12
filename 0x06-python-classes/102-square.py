#!/usr/bin/python3
"""
    Defines a square
"""


class Square:
    """
        Representation of a square
    """
    def __init__(self, size=0):
        """Initialization
            Args:
                size (int): of square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area
        """
        return (self.__size ** 2)

    def __lt__(self, other):
        """less than <"""
        return(self.area() < other.area())

    def __le__(self, other):
        """less or equal than <="""
        return(self.area() <= other.area())

    def __eq__(self, other):
        """equal to =="""
        return(self.area() == other.area())

    def __ge__(self, other):
        """greater or equal than >="""
        return(self.area() >= other.area())

    def __gt__(self, other):
        """greater than >"""
        return(self.area() > other.area())

    def __ne__(self, other):
        """ not equal to !="""
        return(self.area() != other.area())
