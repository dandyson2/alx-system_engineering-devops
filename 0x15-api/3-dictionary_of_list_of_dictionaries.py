#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests


def export_todo_list_to_json():
    # API endpoint URL
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get list of users from the API
    users = requests.get(base_url + "users").json()

    # Create a dictionary to store todo information for all users
    todos_by_user = {}

    # Retrieve todos for each user and organize the data in a dictionary
    for user in users:
        user_id = user.get("id")
        todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

        # Extract relevant information and store in the dictionary
        user_todos = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        } for todo in todos]

        # Add user's todo list to the dictionary
        todos_by_user[user_id] = user_todos

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todos_by_user, jsonfile, indent=4)  # Use indentation for a readable JSON format


# Check if the script is being run directly
if __name__ == "__main__":
    export_todo_list_to_json()
