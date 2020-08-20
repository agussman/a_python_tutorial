#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

'''convert csv input (hardcoded file) to tab-delimited text (stdout)'''

import sys
import csv
import argparse

# GLOBAL SETTINGS
csv.field_size_limit(1000000000)

# GLOBAL VARIABLES
INPUT_DELIMITER = ','
OUTPUT_DELIMITER = '\t'
QUOTECHAR = '"'

def main():

     args = parse_options()

     for input_csv in args.csvs:
          with open(input_csv, 'r') as csvfile:
               # setting skipinitialspace because the demo files have:
               # , "TEXT"
               # instead of
               # ,"TEXT"
               csvreader = csv.reader(csvfile, delimiter=INPUT_DELIMITER, quotechar=QUOTECHAR, skipinitialspace = True)
               csvwriter = csv.writer(sys.stdout, delimiter=args.delimiter, quotechar=QUOTECHAR)
               for row in csvreader:
                    # Clean up leading and trailing whitespace
                    row = [x.strip() for x in row]

                    csvwriter.writerow(row)


def parse_options():
     parser = argparse.ArgumentParser(description='Convert csv files to tab-delimited text (stdout)')
     parser.add_argument('csvs', metavar='N', nargs='+', help="One or more .csv files") # grab the arguments as a list
     parser.add_argument('-d', '--delimiter', dest='delimiter', action="store", default="\t", help="Output delimiter to use")

     return parser.parse_args()


if __name__ == '__main__':
    main()
