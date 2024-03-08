#!/usr/bin/python3
"""Recurse it!"""

import requests

headers = {"User-Agent": "AlxUserAgent/1.0"}

def recurse(subreddit, hot_list=[], after=""):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("data", {}).get("after")
    return recurse(subreddit, hot_list, after) if after else hot_list
