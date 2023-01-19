#!/usr/bin/python3
"""Displays the value of a header response variable"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    print(req.headers['X-Request-Id'])
