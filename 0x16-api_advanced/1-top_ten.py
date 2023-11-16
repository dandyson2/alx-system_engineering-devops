#!/usr/bin/python3
"""Contains the top_ten function"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit for which you want to fetch

    Returns:
        None
    """
    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set headers for the API request
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0\
        (by /u/firdaus_cartoon_jr)"
    }

    # Set parameters for the API request, limiting the results to 10 posts
    params = {
        "limit": 10
    }

    # Send a GET request to Reddit API to retrieve the top posts
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit exists (status code 404) and handle accordingly
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the data containing post information
    results = response.json().get("data")

    # Print the titles of the top 10 posts
    [print(post.get("data").get("title")) for post in results.get("children")]
