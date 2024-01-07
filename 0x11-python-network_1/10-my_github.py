#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    if len(argv) >= 3:
        user = argv[1]
        url = "https://api.github.com/users/{user}".format(user=user)
        token = argv[2]
        headers = {'Authorization': f'Basic {user}:{token}',
                   'Accept': 'application/vnd.github.v3+json'
                   }
        res = get(url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            print(data.get('id'))
        else:
            print("None")
