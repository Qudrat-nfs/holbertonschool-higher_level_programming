#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode("utf-8"))
