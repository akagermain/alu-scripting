#!/usr/bin/python3
"""Recursively query the Reddit API and count keywords in hot titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords found in hot titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    response = requests.get(
        url,
        headers=headers,
        params={"limit": 100, "after": after},
        allow_redirects=False
    )
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "")
        for word in title.lower().split():
            counts[word] = counts.get(word, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    totals = {}
    for word in word_list:
        word = word.lower()
        if counts.get(word):
            totals[word] = totals.get(word, 0) + counts[word]

    ordered = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    for word, count in ordered:
        print("{}: {}".format(word, count))
