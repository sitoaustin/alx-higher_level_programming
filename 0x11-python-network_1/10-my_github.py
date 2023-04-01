#!/usr/bin/python3
""" a Python script  that  gets
github user
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    data = requests.get('https://api.github.com/user', auth=basic)
    print(data.json().get("id"))
