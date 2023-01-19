#!/usr/bin/python3
"""Takes GitHub credentials and displays id"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    resp = requests.get(url, auth=(username, password))
    try:
        print(resp.json()["id"])
    except KeyError:
        print("None")
