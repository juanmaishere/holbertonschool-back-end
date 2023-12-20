#!/usr/bin/python3
"""
Summary : Api requesting employee information
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Module for Asking apis info"""
    employee_id = argv[1]
    url_t = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_u = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url_t)
    responseuser = requests.get(url_u)
    sum = 0

    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()
    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()
    employee = response.json()
    employeeinfo = responseuser.json()

    user_id = employeeinfo['id']
    username = employeeinfo['username']

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csw = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee:
            csw.writerow([user_id, username, task['completed'], task['title']])
