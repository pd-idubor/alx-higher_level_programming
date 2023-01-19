#!/usr/bin/python3
"""Challenge"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    head = {'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'}

    resp = requests.get(url, headers=head)

    count = 0
    for val in resp.json():
        if (count > 9):
            break
        print("{}: {}".format(val['sha'],
              val['commit']['author']['name']))
        count += 1
