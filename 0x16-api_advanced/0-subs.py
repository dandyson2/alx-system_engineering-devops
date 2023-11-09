#!/usr/bin/python3
"""
This script contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit for which you want to get the number of subscribers.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if there was an issue with the request.
    """
    # Check if the subreddit is a valid string
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Send a GET request to Reddit API to retrieve subreddit information
    response = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                            headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'})

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    # Parse the JSON response and extract the number of subscribers
    data = response.json()
    subscribers = data.get("data", {}).get("subscribers", 0)

    return subscribers
