#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response using requests.
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    response = requests.post(url, data=values)
    html = response.text
    print(html)
