#!/usr/bin/python3

"""  Python script that takes your Github credentials (username and password)
     and uses the Github API to display your id """

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/users/"
    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]
    url = url+query
    req = requests.get(url)
    json = req.json()
    print(json['id'])
