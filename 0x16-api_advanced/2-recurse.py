#!/usr/bin/python3
"""
Contains recurse function for retrieving titles of hot posts in a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches titles of hot posts on a subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: List to store post titles.
    :param after: Token for paginating through results.
    :param count: Count of posts fetched.
    :return: List of titles of hot posts.
    """
    # Reddit API URL for hot posts in the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # User-Agent header to mimic a web browser
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0\
        (by /u/firdaus_cartoon_jr)"
    }

    # Parameters for the API request
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit exists
    if response.status_code == 404:
        return None

    # Parse the JSON response
    results = response.json().get("data")

    # Update variables for pagination
    after = results.get("after")
    count += results.get("dist")

    # Extract titles and add them to the hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # Recursively call the function if there are more results
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list
