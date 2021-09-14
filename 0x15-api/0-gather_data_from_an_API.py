#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        id_user = argv[1]
        id_url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(id_url, id_user))
        name = req.json().get("name")
        if name is not None:
            jsonreq = requests.get(
                "{}todos?userId={}".format(
                    id_url, id_user)).json()
            alltsk = len(jsonreq)
            taskcompleted = []
            for t in jsonreq:
                if t.get("completed") is True:
                    taskcompleted.append(t)
            count = len(taskcompleted)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in taskcompleted:
                print("\t {}".format(title.get("title")))
