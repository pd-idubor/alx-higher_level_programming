#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sort in sorted(a_dictionary):
        for k, v in a_dictionary.items():
            if k == sort:
                print("{}: {}".format(k, v))
