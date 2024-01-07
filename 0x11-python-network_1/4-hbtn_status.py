#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = get(url)
    body = res.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
