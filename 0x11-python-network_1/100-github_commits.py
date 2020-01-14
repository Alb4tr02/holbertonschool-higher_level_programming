#!/usr/bin/python3

"""  Python script that takes your Github credentials (username and password)
     and uses the Github API to display your id """

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/"
    user = sys.argv[2]
    repo = sys.argv[1]
    url = url + user + "/" + repo + "/commits"
    req = requests.get(url)
    json = req.json()
    cnt = 0
    for res in json:
        print("{}: {}".format(res['sha'], res['commit']['author']['name']))
        cnt = cnt + 1
        if cnt > 9:
            break
