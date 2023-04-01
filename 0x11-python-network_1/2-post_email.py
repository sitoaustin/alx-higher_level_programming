#!/usr/bin/python3
""" a Python script  that takes in a URL and an email,
sends a POST request to the passed URL with the email 
as a parameter, and displays the body of the response 
(decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    url = sys.argv[1]
    data = sys.argv[2]
    req = Request(url, urlencode(data).encode())
    with Request(req) as response:
        content = response.read().decode('utf-8')
        print(content)
    # response = urlopen(req).read().decode()
    # print(response)