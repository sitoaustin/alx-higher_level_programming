#!/usr/bin/python3
""" a Python script  that  gets
github user
"""
import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    pass_w = sys.argv[2]
    params = {"username": user_name, "auth": pass_w}
    res = requests.get("users/{}".format(user_name), data=params)
    print(res)
