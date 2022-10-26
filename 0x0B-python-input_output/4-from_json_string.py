#!/usr/bin/python3
"""
    Defines a functiok that returns a python object
"""
import json


def from_json_string(my_str):
    """Returns the python representation of a json string"""
    return (json.loads(my_str))
