#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from requests import get
from requests.exceptions import RequestException
from sys import argv


if __name__ == "__main__":
    if len(argv) >= 2:
        url = argv[1]
        try:
            res = get(url)
            if res.status_code != 200:
                err_msg = "Error code: {}".format(str(res.status_code))
                raise RequestException(err_msg)
            print(res.text)
        except RequestException as e:
            print(e)
