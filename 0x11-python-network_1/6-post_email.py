#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    val_email = argv[2] if len(argv) >= 3 else ""
    if len(argv) >= 2:
        url = argv[1]
        myobj = {'email': val_email}
        res = post(url, data=myobj)
        print(res.text)
