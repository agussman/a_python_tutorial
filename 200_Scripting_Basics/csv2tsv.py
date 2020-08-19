#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

'''convert csv input (file or stdin) to tab-delimited text (stdout)'''

import csv
import fileinput

# GLOBAL SETTINGS
csv.field_size_limit(1000000000)

# GLOBAL VARIABLES
DELIMITER = ','
QUOTECHAR = '"'

def main():
     #for line in fileinput.input():
     csvreader = csv.reader(fileinput.input(), delimiter=DELIMITER, quotechar=QUOTECHAR)
     for row in csvreader:
          print('\t'.join(row))
          #print '\t'.join(row[0:3])
          #print '\t'.join(row[j] for j in (0,2))

if __name__ == '__main__':
    main()
