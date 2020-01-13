#!/usr/bin/python3

""" Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8) """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    values = {'email': mail}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("{}".format(the_page.decode("utf-8")))
