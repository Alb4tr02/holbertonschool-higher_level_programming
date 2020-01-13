#!/usr/bin/python3

""" Python script that fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    sep = "\t-"
    print("{}".format("Body response:"))
    print("{} {} {}".format(sep, "type:", type(html)))
    print("{} {} {}".format(sep, "content:", html))
    print("{} {} {}".format(sep, "utf8 content:", html.decode("utf-8")))
