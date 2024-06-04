#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url)

    # Check if the response has content and is JSON
    if response.status_code == 200 and response.headers['content-type'] == 'application/json':
        try:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers')
            if subscribers is not None:
                return subscribers
            else:
                print(f"No subscriber count found for subreddit: {subreddit}")
                return None
        except ValueError:
            print(f"Invalid JSON response: {response.content}")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}, content type: {response.headers['content-type']}")
        return None

