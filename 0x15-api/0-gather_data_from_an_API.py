#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID, 
returns information about his/her TODO list progress
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res_1 = get('https://jsonplaceholder.typicode.com/todos/')
    data_1 = res_1.json()
    finsihed = 0
    total = 0
    tasks = []
    res_2 = get('https://jsonplaceholder.typicode.com/users')
    data_2 = res_2.json()

    for i in data_2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data_1:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                finsihed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, finsihed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
