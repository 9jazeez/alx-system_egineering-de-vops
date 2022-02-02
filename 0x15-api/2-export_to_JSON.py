#!/usr/bin/python3

"""This module gathers data from a REST API
It receives an integer as the employee's id
and then displays the employee's to do list.
Output into a JSON file."""

import requests
import sys
import json

if __name__ == "__main__":

    file_json = sys.argv[1] + ".json"
    dict_f = dict()
    list1 = []

    r = requests.request(
      'GET',
      'https://jsonplaceholder.typicode.com/users/' +
      sys.argv[1] + '/todos')

    r2 = requests.request(
       'GET',
       'https://jsonplaceholder.typicode.com/users/' +
       sys.argv[1])

    username = r2.json().get('username')
    user_id = r.json()[0].get('userId')

    for i in r.json():
        c = {"task": i.get('title'),
             "completed": i.get('completed'),
             "username": username}
        list1.append(c)

    dict_f = {str(user_id): list1}

    with open(file_json, "w") as csv_f:
        json.dump(dict_f, csv_f)
