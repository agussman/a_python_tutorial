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
