#!/usr/bin/python3
""" a Python script that takes in a URL,
sends a request to the URL and displays the value of the 
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    user_input = input("Enter username:")
    req = urllib.request.Request('{}'.format(user_input))
    with urllib.request.urlopen(req) as response:
        content = response.headers.items()
        print(content["X-Request-Id"])
