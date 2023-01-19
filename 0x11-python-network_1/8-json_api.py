#!/usr/bin/python3
"""Sends post request with letter as parameter"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) == 2):
        value = sys.argv[1]
    else:
        value = ""
    payload = {'q': value}

    req = requests.post(url, data=payload)
    try:
        r = req.json()
        if (len(r) < 1):
            print("No result")
        else:
            print("[{}] {}".format(r[id], r[name]))
    except ValueError:
        print("Not a valid JSON")
