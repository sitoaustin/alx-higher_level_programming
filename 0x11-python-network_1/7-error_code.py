#!/usr/bin/python3
""" a Python script  that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response))
    else:
        print(response.status_code)
