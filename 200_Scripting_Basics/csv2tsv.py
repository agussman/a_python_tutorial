#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

'''convert csv input (file or stdin) to tab-delimited text (stdout)'''

import sys
import csv
import fileinput

# GLOBAL SETTINGS
csv.field_size_limit(1000000000)

# GLOBAL VARIABLES
INPUT_DELIMITER = ','
OUTPUT_DELIMITER = '\t'
QUOTECHAR = '"'

def main():
     csvreader = csv.reader(fileinput.input(), delimiter=INPUT_DELIMITER, quotechar=QUOTECHAR)
     csvwriter = csv.writer(sys.stdout, delimiter=OUTPUT_DELIMITER, quotechar=QUOTECHAR)
     for row in csvreader:
          # Clean up leading and trailing whitespace
          row = [x.strip() for x in row]

          csvwriter.writerow(row)

if __name__ == '__main__':
    main()
