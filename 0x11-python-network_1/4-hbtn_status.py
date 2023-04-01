#!/usr/bin/python3
"""A script that fetches
https://alx-intranet.hbtn.io/status
and uses requests
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    # print("\t- utf8 content: {}".format(response.decode('utf-8')))
