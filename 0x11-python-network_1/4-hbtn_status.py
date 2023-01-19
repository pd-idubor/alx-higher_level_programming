#!/usr/bin/python3
"""Script that returns a url"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    print(req)
    resp = req.content
    print("Body response:")
    print("\t- type: {}".format(type(resp.decode('utf-8'))))
    print("\t- content: {}".format(resp))
