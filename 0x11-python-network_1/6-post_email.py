#!/usr/bin/python3
"""Displays the value of a header response variable"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}

    req = requests.post(url, data=mail)
    print(req.text)
