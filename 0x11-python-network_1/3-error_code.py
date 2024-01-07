#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.error import URLError
from sys import argv


if __name__ == "__main__":
    try:
        url = argv[1]
        with urlopen(url) as res:
            print(res.read().decode("UTF-8"))
    except URLError as e:
        print("Error code: {}".format(e.code))
