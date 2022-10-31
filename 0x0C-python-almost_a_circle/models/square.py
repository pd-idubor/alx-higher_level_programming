#!/usr/bin/python3
"""
    Defines the Square class that inherits from the Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets square size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets width and height"""
        self.validator("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Returns printablr rep of class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
