#!/usr/bin/python3
"""How many subs?"""
import requests

headers = {"User-Agent": "AlxUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        if "data" in response.json() and "subscribers" in response.json()["data"]:
            return response.json().get('data').get('subscribers')
        else:
            return 0
    else:
        return 0
