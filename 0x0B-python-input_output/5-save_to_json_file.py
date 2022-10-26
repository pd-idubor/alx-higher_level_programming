#!/usr/bin/python3
"""
    Defines a function that writes an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json rep."""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(json.dumps(my_obj)))
