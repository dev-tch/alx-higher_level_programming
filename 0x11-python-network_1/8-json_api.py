#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    val_letter = argv[1] if len(argv) >= 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    myobj = {'q': val_letter}
    res = post(url, data=myobj)
    try:
        _dict = res.json()
        if _dict:
            val_id = _dict.get('id')
            val_name = _dict.get('name')
            print("[{id}] {name}".format(id=val_id, name=val_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
