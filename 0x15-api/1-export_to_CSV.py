#!/usr/bin/python3

"""This module gathers data from a REST API
It receives an integer as the employee's id
and then displays the employee's to do list.
Output into a CSV file."""

import requests
import sys
import csv

if __name__ == "__main__":

    file_csv = sys.argv[1] + ".csv"
    r = requests.request(
      'GET',
      'https://jsonplaceholder.typicode.com/users/' +
      sys.argv[1] + '/todos')

    r2 = requests.request(
       'GET',
       'https://jsonplaceholder.typicode.com/users/' +
       sys.argv[1])

    name = r2.json().get('username')

    with open(file_csv, "w") as csv_f:
        wrt = csv.writer(
            csv_f,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        for i in r.json():
            wrt.writerow([
               str(i.get('userId')),
               str(name),
               str(i.get('completed')),
               str(i.get('title'))])
