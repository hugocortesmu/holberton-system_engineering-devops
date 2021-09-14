#!/usr/bin/python3
'''
data in the JSON format
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    id_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    id_user = requests.get(id_url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    todo = requests.get(url, verify=False).json()
    name = id_user.get('username')
    t = [{"task": t.get("title"),
          "username": name,
          "completed": t.get("completed")} for t in todo]
    bj = {}
    bj[uid] = t
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(bj, filejs)
