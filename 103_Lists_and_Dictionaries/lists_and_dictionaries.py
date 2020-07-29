# Python supports compound data types used to group together multiple values

# a `list` is one of those:

fruits = ['apple', 'banana', 'cherry', 'durian', 'emblic']

print(fruits) # ['apple', 'banana', 'cherry', 'durian', 'emblic']

# If you're familiar with the concept of arrays from other programming languages, it's a lot like that

# They are indexable, starting w/ 0
print(fruits[0]) # apple
print(fruits[1]) # banana

# Negative indexes start from the back of the list
print(fruits[-1]) # emblic

# use len() to get then length of a list
print(len(fruits)) # 5

# use slices to get sub-parts of a list as a list
# the sytanx is inclusve of the start index, exclusive of the end index
print(fruits[2:4]) # ['cherry', 'durian']

# leaving out either the start or end index implies the begining or end of the list
print(fruits[:3]) # ['apple', 'banana', 'cherry']
print(fruits[3:]) # ['durian', 'emblic']

# You can also use negative indexes in a slice to "tail" a list
print(fruits[-4:]) # ['banana', 'cherry', 'durian', 'emblic']

# There is no constraint that the elements of list be the same type
motley = ["alpha", 0, 99.99, False]
print(motley) # ['alpha', 0, 99.99, False]

# Add to the end of the list with `append()`
motley.append("caboose")
print(motley) # ['alpha', 0, 99.99, False, 'caboose']

# Insert an element at any point in the list with `insert(index, object)`
motley.insert(0, "engine")
motley.insert(3, "dining car")
print(motley) # ['engine', 'alpha', 0, 'dining car', 99.99, False, 'caboose']

# Some other things that are slightly less common but still useful to do with lists.

# use `pop()` to remove the item from the end of the list and return it
a = motley.pop()
print(a) # caboose
print(motley) # ['engine', 'alpha', 0, 'dining car', 99.99, False]

# You can also provide pop and index to remove and return any item
a = motley.pop(1)
print(a) # alpha
print(motley) # ['engine', 0, 'dining car', 99.99, False]

# `.index(x)` will return the first index whose value is x
i = motley.index('dining car')
print(i) # 2
print(motley[i]) # dining car

# You can combine lists with the + operator
race = [3, 2, 1]
car = ["wheels", "engine", "gas"]

racecar = race + car
print(racecar) # [3, 2, 1, 'wheels', 'engine', 'gas']

# This is not a thing
# racecar - car




# Another useful data type is the Dictionary (aka dict)
# In other languages this might be called an “associative arrays”, "hash", or "map"

# It is best to think of a dictionary as a set of key: value pairs
# keys can be any immutable type (typically strings and numbers)
# values can basically be anything

# Creating a dictionary looks like this
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "durian": "spikey?",
    "emblic": "green"
}

print(fruit_colors) # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'durian': 'spikey?', 'emblic': 'green'}

# Get the value of a given key
banana_color = fruit_colors["banana"]
print(banana_color) # yellow

# Note that this didn't modify the dict
print(fruit_colors) # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'durian': 'spikey?', 'emblic': 'green'}

# We can add a new item to the dict with
fruit_colors["fig"] = "purple"
print(fruit_colors) # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'durian': 'spikey?', 'emblic': 'green', 'fig': 'purple'}

# This is also the same syntax for updating the value of an existing key
fruit_colors["banana"] = "brown"
print(fruit_colors) # {'apple': 'red', 'banana': 'brown', 'cherry': 'red', 'durian': 'spikey?', 'emblic': 'green', 'fig': 'purple'}


# TODO: Rules of thumb for when to use a list vs a dictionary

# The items in a list can be other lists or dictionaries:

list_of_lists = [
    [1,2,3],
    [4,5,6],
    ["seven", "eight", "nine", True]
]

print(list_of_lists)

list_of_dicts = [
    {
        "isbn": "0441172717",
        "title": "Dune",
        "author": "Frank Herbert"
    },
    {
        "isbn": "9780007270422",
        "title": "Foundation",
        "author": "Isaac Asimov",
        "read": True
    }
]
print(list_of_dicts)

# The values in a dict can be lists or dicts as well:

dict_of_lists = {
    "attendees": ["Jill", "Joanie", "Jessica"],
    "notes": [
        "A toaster oven in a broad striped suit.",
        "Eleven total trumpets swollen with malevolence.",
        "If only an even handed man would offer up the time.",
        "It is ever always the way of rainbows and rivers to move in a deterministic fashion."
    ]
}
print(dict_of_lists)

dict_of_dicts = {
    "divinations": 
        {
            "hydropmancy": "water",
            "geomancy": "earth",
            "anthropomancy": "entrails"
        },
    "omics":
        {
            "genomics": "genomes",
            "proteomics": "proteins"
        },
    "temperature":
        {
            "2020-05-01": 85,
            "2020-05-02": 77,
            "2020-05-03": 80
        }
}

print(dict_of_dicts)

# Crucially, you cannot use dicts os lists as the KEY of a dictionary
'''
fail_dict_key = {
    {key: value}: False
}

fail_list_key = {
    [0,1]: False
}
'''

# If you absolutely must use a compound data type as a dict key, you can use something called a tuple 
# We're ignoring tuples for now because I don't think they're all that important
dict_with_tuples = {
    (0,1): "<-- that's an example of a tuple being used as a key",
    ("a", "b", "c"): "<-- here's another tuple being used as a key"
}
print(dict_with_tuples)


# An important thing you will often need to do is check if an item is in a list
# we use "if" and "in" to check this

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if "Monday" in weekdays:
    print("Monday is a weekday") # This will be printed
else:
    print("Monday is not a weekday")

if "Saturday" in weekdays:
    print("Saturday is a weekday")
else:
    print("Saturday is not a weekday") # This will be printed

# To check if it's not in there, use... "not"
if "Slurmsday" not in weekdays:
    print("Yeah, Slurmsday isn't a thing.") # This will print


# Use the same if/in syntax to check if a dict has a specific key
if "apple" in fruit_colors:
    print("apple is a key in fruit_colors") # prints
else:
    print("apple is not a key in fruit_colors")

if "gooseberry" in fruit_colors:
    print("gooseberry is a key in fruit_colors")
else:
    print("gooseberry is not a key in fruit_colors") # prints

if "red" not in fruit_colors:
    print("red is not a KEY in fruit_colors") # prints

# To check if a dict contains a particular value, we use dict.values()
# dict.values() is actually returning a list, which is kind of ironic if you think about it
if "red" in fruit_colors.values():
    print("red is a VALUE in fruit_colors") # prints

# This, of course, begats the question, "How do I know what key has the given value?" to which I say,
# Snarky answer: You're probably doing something wrong if you're trying to do this.
# Less snarky answer: It involves Loops, so hang tight until the Loops lesson.

# One last thing that does come up a lot is that you'll want to check if a key is in a dict
# and return the value if the key is present, otherwise return some other value
# You can do this with dict.get(key, default_value)

# print(fruit_colors["gooseberry"]) # Throws a KeyError

print(fruit_colors.get("gooseberry", "translucent")) # translucent