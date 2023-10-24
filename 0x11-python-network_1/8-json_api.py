#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q': q}

    base_url = "http://0.0.0.0:5000/search_user"
    response = requests.post(base_url, data=data)

    try:
        user_data = response.json()
        if user_data:
            user_id = user_data.get('id')
            user_name = user_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
