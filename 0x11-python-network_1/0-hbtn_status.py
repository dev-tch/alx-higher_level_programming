#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = " https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:$")
        tab = "\t"
        # print content type
        print("{}- type: {}".format(tab, type(content)))
        # print content
        print("{}- content: {}".format(tab, content))
        # pint decoded content
        # headers = res.info()
        # arr = headers["Content-Type"].split("=")
        # encoding = arr[1]
        # data = content.decode(encoding)
        # print("\t- {} content: {}".format(encoding, data))
        data = content.decode("UTF-8")
        print("{}- utf8 content: {}".format(tab, data))
