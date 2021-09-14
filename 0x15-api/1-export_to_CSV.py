#!/usr/bin/python3
'''
extend your Python script to export data in the CSV format
'''

import csv
import requests
from sys import argv


if __name__ == '__main__':
    uid = argv[1]
    id_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    id_user = requests.get(id_url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            taskwriter.writerow([int(uid), id_user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
