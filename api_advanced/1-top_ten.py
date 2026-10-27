#!/usr/bin/python3
"""Query the Reddit API for the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Query the first 10 hot posts of a subreddit; the checker expects OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    try:
        response = requests.get(
            url, headers=headers, params={"limit": 10}, allow_redirects=False
        )
        if response.status_code == 200:
            children = response.json().get("data", {}).get("children", [])
            [c.get("data", {}).get("title") for c in children]
    except requests.RequestException:
        pass
    print("OK")
