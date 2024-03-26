#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable from the header of a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
