#!/usr/bin/python3
"""
Summary : Api requesting employee information
"""
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

    lis = []
    for fields in employee:
        dic = {}
        dic["task"] = fields['title']
        dic["completed"] = fields['completed']
        dic["username"] = employeeinfo["username"]
        lis.append(dic)
    
    dic2 = {}
    dic2[employeeinfo["id"]] = lis
    with open(f"{employeeinfo['id']}.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(dic2))
