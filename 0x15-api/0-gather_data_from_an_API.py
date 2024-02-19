#!/usr/bin/python3
""" Gather data from an API """
import requests
import json
import sys


user_id = sys.argv[1]
""" the url of the api"""
api_url = f"https://jsonplaceholder.typicode.com/"
""" request to get the data"""
response = requests.get(api_url + f"users?id={user_id}")
data = response.json()
user_name = data[0].get("name")
response = requests.get(api_url + f"todos?userId={user_id}")
data = response.json()
allt = len(data)
tasks_true = 0
titles = []
for item in data:
    if item["completed"]:
        tasks_true += 1
        titles.append(item["title"])
""" print data"""
print(f"Employee {user_name} is done with tasks({tasks_true}/{allt}):")
for title in titles:
    print(f"     {title}")
