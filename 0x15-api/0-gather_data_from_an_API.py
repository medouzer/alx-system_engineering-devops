#!/usr/bin/python3
""" Gather data from an API """
import requests
import json
import sys


user_id = sys.argv[1]
print(user_id)
api_url = f"https://jsonplaceholder.typicode.com/"
response = requests.get(api_url + f"users?id={user_id}")

if response.status_code == 200:
    data = response.json()
    user_name = data[0].get("name")
    response = requests.get(api_url + f"todos?userId={user_id}")
    if response.status_code == 200:
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
    else:
        print("Request failed with status code:", response.status_code)

else:
    print("Request failed with status code:", response.status_code)
