#!/usr/bin/python3
""" Export to JSON """
import requests
import sys


if __name__ == "__main__":
    """Python script to export data in the CSV format."""
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url + "users/" + user_id)
    user_name = response.json()["username"]
    response = requests.get(api_url + "todos?userId=" + user_id)
    data = response.json()
    allt = len(data)
    tasks_true = 0
    titles = []
    for item in data:
        if item["completed"]:
            tasks_true += 1
            titles.append(item["title"])
    """Export into csv"""
    with open(f'{user_id}.csv', 'w') as file:
        for todo in data:
            p1 = f'"{user_id}","{user_name}","{todo.get("completed")}",'
            p2 = f'"{todo.get("title")}"\n'
            file.write(p1+p2)
