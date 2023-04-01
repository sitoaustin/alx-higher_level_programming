#!/usr/bin/python3
""" a Python script  that  gets
github user
"""
import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    pass_w = sys.argv[2]
    login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(user_name,pass_w))
    print(dict(login.text).get("items"))
