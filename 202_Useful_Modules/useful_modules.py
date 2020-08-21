# random numbers
import random

# Print 5 random integers between 0 and 9, inclusive
for i in range(5):
    print(random.randrange(0, 10))

# json
import json

txt = '{ "id": 300, "name": "Nancy", "scores": [3.4, 2.9, 4.4, 3.4]}'
j = json.loads(txt)
for key, value in j.items():
    print(f"Key: {key} -> Value: {value}")

# csv
import csv

input_csv = "../201_Command-line_Interfaces/data/va_cities.csv"
with open(input_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row[8])


# requests
# https://requests.readthedocs.io/en/master/
# This is not a built-in module, you'll need to install it