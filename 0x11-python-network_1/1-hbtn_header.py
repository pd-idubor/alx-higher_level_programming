#!/usr/bin/python3
"""Displays the value of a header response variable"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.getheader('X-Request-Id')
        print("{}".format(header))
