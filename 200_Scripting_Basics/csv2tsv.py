#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

'''convert csv input (hardcoded file) to tab-delimited text (stdout)'''

import sys
import csv

# GLOBAL SETTINGS
csv.field_size_limit(1000000000)

# GLOBAL VARIABLES
INPUT_FILE = "data/ND_airport_runways.csv"
INPUT_DELIMITER = ','
OUTPUT_DELIMITER = '\t'
QUOTECHAR = '"'

def main():

     with open(INPUT_FILE, 'r') as csvfile:
          csvreader = csv.reader(csvfile, delimiter=INPUT_DELIMITER, quotechar=QUOTECHAR)
          csvwriter = csv.writer(sys.stdout, delimiter=OUTPUT_DELIMITER, quotechar=QUOTECHAR)
          for row in csvreader:
               # Clean up leading and trailing whitespace
               row = [x.strip() for x in row]

               csvwriter.writerow(row)

if __name__ == '__main__':
    main()
