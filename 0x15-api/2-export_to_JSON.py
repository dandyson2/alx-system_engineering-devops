#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys


def export_todo_list(user_id):
    # API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch user's todos
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Prepare data and write to JSON file
    data = {
        user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]
    }

    # Write data to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)  # Indent for pretty formatting


if __name__ == "__main__":
    # Check if user ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    # Get user ID from command-line argument
    user_id = sys.argv[1]

    # Call the export function with the provided user ID
    export_todo_list(user_id)
