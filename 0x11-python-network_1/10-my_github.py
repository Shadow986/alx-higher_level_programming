#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
