#!/usr/bin/python3

"""
Using task #0, extend your Python script to export data in the JSON format
"""

from requests import get
import json

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    data_1 = res.json()

    row = []
    res_2 = get('https://jsonplaceholder.typicode.com/users')
    data_2 = res_2.json()

    new_dict1 = {}

    for j in data_2:

        row = []
        for i in data_1:

            new_dict2 = {}

            if j['id'] == i['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)

        new_dict1[j['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
