#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script 
to export data in the CSV format.
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    data = res.json()

    row = []
    res_2 = get('https://jsonplaceholder.typicode.com/users')
    data_2 = res_2.json()

    for i in data_2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)
