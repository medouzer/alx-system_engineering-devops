#!/usr/bin/python3
""" Gather data from an API """
import json
import requests
import sys


if __name__ == "__main__":
    """ request the data and print it"""
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url + "users/" + user_id)
    user_name = response.json()["username"]
    response = requests.get(api_url + "todos?userId=" + user_id)
    data = response.json()
    allt = len(data)
    tasks_true = 0
    users = []
    for user in data:
        tasks_dict = {}
        tasks_dict["task"] = user["title"]
        tasks_dict["completed"] = user["completed"]
        tasks_dict["username"] = user_name
        users.append(tasks_dict)
    final_data = {user_id: users}
    with open(user_id + ".json", "w") as jsonfile:
        json.dump(data, jsonfile)
