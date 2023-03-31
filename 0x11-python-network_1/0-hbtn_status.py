#!/usr/bin/python3
"""A script that fetches 
https://alx-intranet.hbtn.io/status
and uses urllib library
"""

import urllib.request

if __name__ == "__main__":
    the_page = ""
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
