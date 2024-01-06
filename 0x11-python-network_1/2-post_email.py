#!/usr/bin/python3
"""
Write a Python script that takes
in a URL and an email, sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    val_email = argv[2] if len(argv) >= 3 else ""
    if len(argv) >= 2:
        url = argv[1]
        values = {'email': val_email}
        param = urlencode(values)
        param = param.encode('ascii')  # param should be bytes
        req = Request(url, param)
        with urlopen(req) as res:
            body = res.read()
            # print utf8 body
            print(body.decode("UTF-8"))
