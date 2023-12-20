#!/usr/bin/python3
import requests
from sys import argv
import json

if __name__ == "__main__":

    employee_id = argv[1]
    url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos" 
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url_todos)
    responseuser = requests.get(url_user)
    sum = 0

    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()
    employee = response.json()
    employeeinfo = responseuser.json()
    name = employeeinfo['name']
    for task in employee:
        if task['completed'] == True:
            sum += 1
    print(f"Employee {name} is done with tasks({sum}/{len(employee)}):")
    for task in employee:
        if task['completed'] == True:
            print(f"\t {task['title']}")
