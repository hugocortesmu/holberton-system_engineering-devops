#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the number of subscribers """
import requests
import sys


def number_of_subscribers(subreddit):
    """ Returns: number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
