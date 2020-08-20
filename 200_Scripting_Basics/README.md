# Overview

Creating a Python Script

Shebang, main, executability

# Instructions

Look at the content of the script using your editor.

Then run the script to see the output.
```bash
$ python csv2tsv.py
```

Since this is a script with a shebang line, you can also do:
```bash
$ ./csv2tsv.py
```

If that fails with some message pertaining to excutability, you may need to do:
```bash
$ chmod +x csv2tsv.py
```
to make it executable (this is a Linux/Unix thing, not a Python thing)

You should also take a look at the data file it's reading, to make sense of what it's doing:
```bash
$ cat data/data/ND_airport_runways.csv
```
Then look at the content of script again to make sure you understand what it did.

Here are some things to note:

## Shebang

The script starts with what is called a shebang line:
```
#!/usr/bin/env python3 
```

This tells the shell (`bash`) how to execute the script.

This is a "linux thing" and is not unique to Python. If you were to execute a script written in bash you would use a shebang at the top of:
```
#!/bin/bash
```

Another common shebang you might see is:
```
#!/usr/local/bin/python
```

Although the one called `env` to find the python interpreter is the "correct" approach

## main()

Typically at the bottom of python programs/scripts (e.g., a file that is meant to be executed or run), you will see:
```
if __name__ == '__main__':
    main()
```

This is basically saying, "If you are running me as a script, you should go to the `main()` function and do that".

Of course, for that to work, you actually have to have a `main()` function, which this script does as well.

Python files that are purely library files / modules generally don't have a `main()`. And, because Python is wild, you can still `include` content from a python file with a `if __name__ == '__main__':`, it doesn't prevent any of that.



