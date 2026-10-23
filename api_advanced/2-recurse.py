#!/usr/bin/python3
"""Recursively query the Reddit API for the titles of all hot articles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot articles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    response = requests.get(
        url,
        headers=headers,
        params={"limit": 100, "after": after},
        allow_redirects=False
    )
    if response.status_code != 200:
        return hot_list or None

    data = response.json().get("data", {})
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
