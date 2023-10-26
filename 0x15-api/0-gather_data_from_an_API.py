#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    return user, completed_tasks, len(todos)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        employee_id = sys.argv[1]
        user_info, completed_tasks, total_tasks = get_todo_list(employee_id)
        print("Employee {} is done with tasks ({}/{}):".format(
            user_info.get("name"), len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task))
