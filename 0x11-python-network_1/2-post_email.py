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
    # url = 'https://httpbin.org/post' # Set destination URL here
    # data = {'name': 'Bruce Wayne'}     # Set POST fields here
    req = Request(url, urlencode(data).encode())
    response = urlopen(req).read().decode('utf-8')
    print(response)