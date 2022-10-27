#!/usr/bin/python3
"""
    Adds all args to a list, then save to a file
"""
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    """Adds args to a json file"""
    try:
        content = load_from_json(filename)
    except FileNotFoundError:
        content = []

    for item in args:
        content.append(item)
    save_to_json(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
