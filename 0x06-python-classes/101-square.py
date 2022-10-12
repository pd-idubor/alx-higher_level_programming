#!/usr/bin/python3
"""
    Defines a square
"""


class Square:
    """
        Representation of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization
            Args:
                size (int): of square
                position (tuple): square position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position property to 'value'
        """
        if (isinstance(value, tuple) and len(value) == 2):
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints a representation of the square using '#'
        """
        if (self.__size == 0):
            return ("")

        for lin in range(self.__position[1]):
            print()

        for i in range(self.__size - 1):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

        return ("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        return (self.my_print())
