#!/usr/bin/python3
"""Displays response and handles error"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print(data.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
