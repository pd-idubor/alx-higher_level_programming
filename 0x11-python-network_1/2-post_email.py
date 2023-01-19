#!/usr/bin/python3
"""Displays the value of a header response variable"""
import urllib.request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = urlencode(mail)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print("Your email is: {}".format(resp.decode("utf-8")))
