#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    req = requests.post(url, data={'q': q})
    try:
        json = req.json()
        try:
            print("[{}] {}".format(json['id'], json['name']))
        except KeyError:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
