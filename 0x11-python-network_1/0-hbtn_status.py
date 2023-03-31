#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    the_page = ""
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        print(response.read())
        print(response.read())
        print(response.read())
