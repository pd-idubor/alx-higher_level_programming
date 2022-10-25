#!/usr/bin/python3
"""Defines a class Rectangle inheriting from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Description"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
