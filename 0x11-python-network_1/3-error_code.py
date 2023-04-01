#!/usr/bin/python3
""" a Python script  that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.parse
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try: req = urllib.request.Request(url)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())