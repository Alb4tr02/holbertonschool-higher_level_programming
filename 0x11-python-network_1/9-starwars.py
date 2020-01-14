#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search="
    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]
    url = url+query
    req = requests.get(url)
    json = req.json()
    results = json['results']
    print("Number of results: {}".format(json['count']))
    for person in results:
        print("{}".format(person['name']))
