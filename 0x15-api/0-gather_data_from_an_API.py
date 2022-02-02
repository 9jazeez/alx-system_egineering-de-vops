#!/usr/bin/python3

"""This module gathers data from a REST API
It receives an integer as the employee's id
and then displays the employee's to do list"""

import requests
import sys

if __name__ == "__main__":

    r = requests.request(
      'GET',
      'https://jsonplaceholder.typicode.com/users/' +
      sys.argv[1] + '/todos')

    r2 = requests.request(
       'GET',
       'https://jsonplaceholder.typicode.com/users/' +
       sys.argv[1])

    name = r2.json().get('name')
    done = 0
    undone = 0
    for i, a in enumerate(r.json()):
        if (a.get('completed') is True):
            done += 1
        else:
            undone += 1

    print("Employee {} is done with tasks({}/{}):".format(
           name,
           done,
           undone + done))
    for i in r.json():
        if (i.get('completed') is True):
            print("\t {}".format(i.get('title')))
