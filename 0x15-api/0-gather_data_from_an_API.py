#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys


if __name__ == "__main__":
    """ request the data and print it"""
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url + "users/" + user_id)
    user_name = response.json()["name"]
    response = requests.get(api_url + f"todos?userId={user_id}")
    data = response.json()
    allt = len(data)
    tasks_true = 0
    titles = []
    for item in data:
        if item["completed"]:
            tasks_true += 1
            titles.append(item["title"])
    print(f"Employee {user_name} is done with tasks({tasks_true}/{allt}):")
    for title in titles:
        print(f"     {title}")
