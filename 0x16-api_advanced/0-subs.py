#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    # Define the base URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up headers including a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "Custom User Agent"
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the subscriber count from the parsed JSON
            subscriber_count = data['data']['subscribers']

            # Return the subscriber count
            return subscriber_count
        else:
            # If the request was not successful, return 0
            return 0
    except Exception as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return 0

