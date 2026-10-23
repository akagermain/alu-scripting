#!/usr/bin/python3
"""Query the Reddit API and print the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url, headers=headers, params={"limit": 10}, allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    for child in response.json().get("data", {}).get("children", []):
        print(child.get("data", {}).get("title"))
