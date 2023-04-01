#!/usr/bin/python3
""" a Python script  that  takes in a 
letter and sends a POST request to 
http://0.0.0.0:5000/search_user with 
the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    if not sys.argv[1]:
        input_payload = ""
    else:
        input_payload = sys.argv[1]
    payload = {'q': input_payload}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    print(response.text)
