# To support code reuse and a, uh, modular structure, Python supports Modules
# A module is a file containing Python definitions and statements.
# There are many built-in modules to Python, aka the Standard Library.
# You can also easily create and use your own modules.

# use a module, we use the `import` statement
import json
# This imports the `json` standard library, allowing us to perform manipulations with json

# We can now use functions from the json library (technically, this is a "Package", not a Module, more on that later)

# Within the json package is a function called `loads()`. We access it with dot syntax.
# `json.loads()` will convert a valid json string into a Python object
txt = '{ "id": 300, "name": "Nancy", "scores": [3.4, 2.9, 4.4, 3.4]}'
j = json.loads(txt)
for key, value in j.items():
    print(f"Key: {key} -> Value: {value}")

# Traditionally all the import statements are at the top of the script, but because this is a didactic exercise
# we will be eschewing that convention

# The `glob` module provides a function for making file lists from directory wildcard searches
import glob

# Within the `glob` module is a function called glob that does the actual, uhh, globbing:
md_files = glob.glob("../*/*.md")
print(md_files)

# If you want to access a specific function or object from a module, you use the `from... import...` syntax:
from glob import glob

# Now we can just do:
py_files = glob("../*/*.py")
print(py_files)


# Creating a module is pretty straightforward

# Look at the contents of `module_a.py` in this directory, it contains two functions from the Functions lesson.
import module_a
# We can now do
print( module_a.are_valid_triangle_side_lengths(3,4,5) ) # True
print( module_a.is_right_triangle(4,5,6) ) # False

# Creating a Package is really just creating a directory with module files in it
# Look at the contents of pacakge_p
'''
107_Modules $ ls -1 package_p/
__init__.py
module_b.py
module_c.py
'''

from package_p import module_b, module_c

module_b.b_message() # Greetings from package_p.module_b!
module_c.c_message() # Greetings from package_p.module_c!

# __init__.py is a special file used to tell python to treat the directory as a package containing modules


