#!/usr/bin/python3
"""
    Defines the representation of a rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        rect = ""
        sym = str(self.print_symbol)

        if (self.__width == 0 or self.__height == 0):
            return (rect)

        for i in range(self.__height - 1):
            rect += (sym * self.__width + "\n")
        rect += (sym * self.__width)
        return (rect)

    def __repr__(self):
        ret = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return (ret)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
