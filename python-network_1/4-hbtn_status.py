#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the requests package.
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
