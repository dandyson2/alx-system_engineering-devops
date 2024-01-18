#!/usr/bin/python3



""" A function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0."""


import requests

def get_subreddit_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number of subscribers for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: Number of subscribers for the subreddit.
    - None: If the subreddit is invalid or an error occurs during the API request.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers={"User-Agent": "YourApp"})  # Replace "YourApp" with your application name
        response.raise_for_status()  # Raise an exception for bad requests
        subreddit_data = response.json()["data"]
        subscribers = subreddit_data["subscribers"]
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage:
subreddit_name = "python"
subscribers_count = get_subreddit_subscribers(subreddit_name)

if subscribers_count is not None:
    print(f"The subreddit r/{subreddit_name} has {subscribers_count} subscribers.")
else:
    print(f"Invalid subreddit: {subreddit_name}")
