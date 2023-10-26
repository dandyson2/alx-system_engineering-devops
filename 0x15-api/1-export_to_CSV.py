#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def export_todo_list_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
    else:
        user_id = sys.argv[1]
        export_todo_list_to_csv(user_id)
