#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    if len(argv) >= 3:
        user = argv[1]
        token = argv[2]
        url = "https://api.github.com/user"
        auth = HTTPBasicAuth(user, token)
        res = get(url, auth=auth)
        if res.status_code == 200:
            data = res.json()
            print(data.get('id'))
        else:
            print("None")
