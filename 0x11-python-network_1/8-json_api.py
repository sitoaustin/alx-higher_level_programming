#!/usr/bin/python3
""" a Python script  that  takes in a
letter and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_payload = sys.argv[1]
    else:
        input_payload = ""
    payload = {'q': input_payload}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response.raise_for_status()
        json = response.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
