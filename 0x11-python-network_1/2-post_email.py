#!/usr/bin/python3
"""Displays the value of a header response variable"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    req = urllib.request.Request(url, mail)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Your email is: {}".format(page))
