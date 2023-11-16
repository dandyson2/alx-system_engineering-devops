#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    A function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    # Initialize word_dict if not provided
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    # If after is None, print the sorted word count and exit
    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    # Construct Reddit API URL and set request parameters
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}

    # Make the API request
    response = requests.get(url, headers=header, params=parameters, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        return None

    try:
        # Extract relevant data from the API response
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']

        # Process each post's title for keyword count
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    # Recursive call to fetch more posts
    count_words(subreddit, word_list, aft, word_dict)
