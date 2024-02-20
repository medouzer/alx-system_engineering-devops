#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    data = {}

    for user_id in range(1, 11):
        response = requests.get(url + "users/" + f"{user_id}")
        user_name = response.json()["username"]

        response = requests.get(url + "todos?userId=" + f"{user_id}")
        todo_list = response.json()

        tasks = []

        for task in todo_list:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user_name
            tasks.append(task_dict)

        data.update({user_id: tasks})

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
