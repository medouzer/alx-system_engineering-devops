#!/usr/bin/python3
""" Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    response = requests.get(base_url + "users/" + user_id)
    user_name = response.json()["name"]

    response = requests.get(base_url + "todos?userId=" + user_id)
    todo_list = response.json()

    completed_tasks = 0
    total_tasks = len(todo_list)

    completed_titles = []

    for task in todo_list:
        if task["completed"]:
            completed_tasks += 1
            completed_titles.append(task["title"])

    print("Employee {} is done with tasks({}/{}):".format(
                                                            user_name,
                                                            completed_tasks,
                                                            total_tasks))

    for title in completed_titles:
        print("\t {}".format(title))
