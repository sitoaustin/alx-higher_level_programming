#!/usr/bin/python3
""" a Python script  that  gets
commits
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(sys.argv[2], sys.argv[1]))
    datas = response.json()
    try:
        for i in range(10):
            print(f"{datas[i]['sha']}: {datas[i]['commit']['author']['name']}")
    except IndexError:
        pass
