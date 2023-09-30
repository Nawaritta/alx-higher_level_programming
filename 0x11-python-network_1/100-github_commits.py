#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest)of the repository
“rails” by the user “rails” using the GitHub API.
"""
import sys
import requests

if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(api_url)
    commits = response.json()
    try:
        for i in range(10):
            print(f"{commits[i].get('sha')}: ", end='')
            print(f"{commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
