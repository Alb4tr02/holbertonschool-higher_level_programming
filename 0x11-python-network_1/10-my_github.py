#!/usr/bin/python3

"""  Python script that takes your Github credentials (username and password)
     and uses the Github API to display your id """

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/users/"
    user = sys.argv[1]
    password = sys.argv[2]
    url = url+user
    req = requests.get(url, auth=(url, password))
    json = req.json()
    try:
        print(json['id'])
    except KeyError:
        print("None")
