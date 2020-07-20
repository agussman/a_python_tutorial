# Here are some things about strings in Python
# This lesson isn't strictly crucial, but it is useful

# You can use single or double quotes to enclose strings in Python, it doesn't matter
print("This is a string.\nHere is the next line.")
print('This is a string.\nHere is the next line.')

# As apostrophes (aka single quotes) show up in contractions, I tend to default to using "
print("Here's a string. It's fine.")

# You can escape the string quoting character with \
print('Here\'s a string. It\'s fine.')
print("They said, \"Yes\"")

# String concatenation uses the + operator
text1 = "Lisa needs braces."
text2 = "Dental plan."
print(text1 + "\n" + text2)

# You can also use the * operator to repeat strings
print("HO"*3)
print( 3 * (text1 + "\n" + text2 + "\n") )

# This next section is taken word for word (heh.) from 
# [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html#strings)

# Strings can be indexed (subscripted), with the first character having index 0. 
# There is no separate character type; a character is simply a string of size one:
word = 'Python'
print(word[0]) # P
print(word[5]) # n

# Indices may also be negative numbers, to start counting from the right:
print(word[-1]) # last character 'n'
print(word[-2]) # penultimate character 'o''

# You can get substrings using slicing
print(word[0:2]) # Py
print(word[2:5]) # tho

# Slice indices have useful defaults; an omitted first index 
# defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:2]) # Py
print(word[2:]) # thon

# Note how the start is always included, and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s
i = 4
print(word[:i]) # Pyth
print(word[i:]) # on

# You can also use negative indexes in your slices
print(word[-3:]) # hon

# The built-in function len() returns the length of a string:
print(len(word)) # 6
print(len(text1[-7:])) # 7

# While len() accepts a string, there a number of methods you can call on string 
text3 = "Red Alert!"
print(text3.upper()) # RED ALERT!
print(text3.lower()) # red alert!
print(text3.startswith("Red")) # True
print(text3.endswith("Alert!")) # True
print(text3.endswith("alert!")) # False (case sensitive)
print(text3.replace("Red", "Yellow")) # Yellow Alert!
print(text3.replace("e", "a", 1)) # Rad Alert! (one replacement)
print("User input often has trailing spaces  ".rstrip()) # "User input often has trailing spaces
print("   Or leading spaces".lstrip()) # Or leading spaces
print("   Or both.  ".strip()) # Or both.

# It's often useful to clean up data for comparisons / aggregate statistics
# by forcing the case and stripping spaces:
print(" Aaron".strip().lower() == "AARON        ".strip().lower()) # True

# join and split are fantastically useful

# Here's join
stuff = ["foo", "bar", "baz"]
print( "-".join(stuff) ) # foo-bar-baz

who = ["Moon", "Townshend", "Daltrey", "Entwistle"]
print(" & ".join(who)) # Moon & Townshend & Daltrey & Entwistle

# For some reason the join syntax always looks weird to me.
# About 25% of the time I think it's a list method and not a string method.

# split is more straightforward
list_of_notes = "do-re-mi-fa-so-la-ti-do".split('-')
print(list_of_notes) # ['do', 're', 'mi', 'fa', 'so', 'la', 'ti', 'do']
print(list_of_notes[3]) # fa

# split is great for all sorts of quick and dirty tasks
year, month, day = "1906-04-18".split('-')
print(month) # 04

parts = "43!!Paxillin!!22.99!!#0000FF".split("!!")
print(parts) # ['43', 'Paxillin', '22.99', '#0000FF']

last_dir_name = "/some/directory/path/on/a/system".split("/")[-1]
print(last_dir_name) # system

# I should point out that there are fairly standard Python libraries
# that much better suited for the above tasks. Like, if there's a trailing /
# the directory parsing isn't going to work right.

# There are many ways to print out variables in a string.

# Here's the old Python 2 style format. You'll probably see this in 
# code you come across. It still works.
name = "John Carter"
print("Welcome to Mars, %s" % name)

# Here's the more modern formatting using .format()
name = "Fortunato"
print("Welcome to my wine cellar, {}".format(name))

wine = "Médoc"
location = "vestibule"
print("Let us try the {}, it is in the {}.".format(wine, location))

# If you know you'll be running your code in Python 3.6 or later
# you can use f-strings:
wine = "Amontillado"
location = "catacombs"
print(f"Let us try the {wine}, it is in the {location}.")

# f strings are pretty cool, and if you use them, then you are pretty cool, too

# There are many options with format()

# Zero padding
print("Up to 4 digits with zero-padding: {:04d}".format(1)) # 0001

# Number of decimal places
print("Round to 3 decimal places: {:.2f}".format(20/3)) # 6.67

# They also play nicely with f-strings
trial = 31
estimate = 22 / 7
print(f"Test subject {trial:06d} had a ratio of {estimate:.4f}.")

