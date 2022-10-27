#!/usr/bin/python3
"""
    Defines a student class
"""


class Student:
    """Student definition"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary rep of 'Student' class"""
        return (self.__dict__)
