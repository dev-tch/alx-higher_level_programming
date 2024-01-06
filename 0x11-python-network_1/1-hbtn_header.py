#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    if len(argv) >= 2:
        # argv[0] ==> name of script
        url = argv[1]
        with urllib.request.urlopen(url) as res:
            headers = res.info()
            if headers["X-Request-Id"]:
                print(headers["X-Request-Id"])
