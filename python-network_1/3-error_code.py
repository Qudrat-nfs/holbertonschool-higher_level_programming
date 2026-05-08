#!/usr/bin/python3
"""
Sends a request to a URL and handles HTTPError exceptions.
"""
from urllib.error import HTTPError
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
