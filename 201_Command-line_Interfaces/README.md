# Overview

argparse

# Instructions

Look at the content of the script using your editor.

Then run the script as so:
```bash
$ ./csv2tsv.py -h
```

You should see the following output:

```
$ ./csv2tsv.py -h
usage: csv2tsv.py [-h] [-d DELIMITER] N [N ...]

Convert csv files to tab-delimited text (stdout)

positional arguments:
  N                     One or more .csv files

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        Output delimiter to use
```

(if you get an error message about executability, you'll likely need to do `chmod +x csv2tsv.py`)

Now try running the script with an input csv:
```
$ ./csv2tsv.py data/va_cities.csv
```

You can even give it more than one:
```
$ ./csv2tsv.py data/va_cities.csv data/ca_cities.csv
```

Instead of a tab, you can specify the delimiter to use in the output:
```
$ ./csv2tsv.py -d "|" data/va_cities.csv data/ca_cities.csv
```

Then look at the content of script again to make sure you understand what it did.