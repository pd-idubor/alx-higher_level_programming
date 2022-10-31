#!/usr/bin/python3
"""
    Defines 'Base' class
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class initialization"""
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dict"""
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")

        return (json.dumps(list_dictionaries))
