#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter 'q'.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if not json_data:
            print("No result")
        # Əgər gələn cavab birbaşa lüğətdirsə (dict)
        elif isinstance(json_data, dict):
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        # Əgər gələn cavab siyahıdırsa (list)
        elif isinstance(json_data, list):
            for user in json_data:
                print("[{}] {}".format(user.get('id'), user.get('name')))

    except ValueError:
        print("Not a valid JSON")
