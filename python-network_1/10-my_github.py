#!/usr/bin/python3
"""
Uses the GitHub API to display the user ID based on given credentials.
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    # Basic Authentication istifadə edərək GET sorğusu göndəririk
    response = requests.get(url, auth=(username, token))
    try:
        json_data = response.json()
        # JSON cavabından 'id' dəyərini götürüb çap edirik
        print(json_data.get('id'))
    except ValueError:
        print("Not a valid JSON")
