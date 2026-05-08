#!/usr/bin/python3
"""
Module to fetch posts from an API and print or save them to CSV.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and displays the titles of all posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to 'posts.csv'
    with columns: id, title, body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        filename = "posts.csv"
        fields = ['id', 'title', 'body']
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(structured_data)
