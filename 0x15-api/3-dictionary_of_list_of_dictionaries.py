#!/usr/bin/python3

"""This module gathers data from a REST API
It stores all the users to do list. """


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
       'https://jsonplaceholder.typicode.com/users/')

    for i in r2.json():
        print(i)


    #with open(file_json, "w") as csv_f:
        #json.dump(dict_f, csv_f)
