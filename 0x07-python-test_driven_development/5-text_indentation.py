#!/usr/bin/python3
"""
    Defines a function that prints a text
"""


def text_indentation(text):
    """Prints a text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tmp = ""
    for char in text:
        tmp += char
        if (char in ".?:"):
            while (tmp[0] == " "):
                tmp = tmp[1:]
            print(tmp)
            print()
            tmp = ""

    if (len(tmp) != 0):
        while (tmp[0] == " "):
            tmp = tmp[1:]
        print(tmp, end="")
