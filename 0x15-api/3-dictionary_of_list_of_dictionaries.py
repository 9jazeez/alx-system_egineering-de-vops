#!/usr/bin/python3

"""This module gathers data from a REST API
It stores all the users to do list. """


import requests
import sys
import json

if __name__ == "__main__":

    dict_f = {}

    r = requests.request(
      'GET',
      'https://jsonplaceholder.typicode.com/todos')

    r2 = requests.request(
       'GET',
       'https://jsonplaceholder.typicode.com/users')

    for user in r2.json():
        list1 = []
        for todo in r.json():
            if user['id'] == todo['userId']:
                dict_in = {}
                dict_in['task'] = todo['title']
                dict_in['completed'] = todo['completed']
                dict_in['username'] = user['username']
                list1.append(dict_in)
        dict_f[user['id']] = list1

    with open('todo_all_employees.json', "w") as csv_f:
        json.dump(dict_f, csv_f)
