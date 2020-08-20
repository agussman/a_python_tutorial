# Very often we will want to perform some action a certain number of times.
# We can use Loops to do that.

# A `while` loop executes as long as a certain condition is true
i = 0
while ( i < 3):
    print("Aye aye captain!")
    print(i)
    i += 1

# A `for` loop executes for each item in a list (or, more broadly, it will execute for each object in an "iterator")
bagel_flavors = ["seasme", "raisin", "everything"]
for flavor in bagel_flavors:
    print(flavor)

# If a function returns a list or iterable object, you can loop over that

# the range function returns a list of integers (inclusive of start, exclusive of end)


# Using range is how we can get the functionality of the traditional `for` loop
for i in range(0, 3):
    print(i*i) # 0, 1, 4

# We can provide an optional increment value
even_numbers = range(0, 10, 2)
# print(even_numbers) # because this is an iterator, it doesn't print what you'd think!
for i in even_numbers:
    print(i) # 0, 2, 4, ... 8


# `for` loops can be nested
for x in [1, 2, 3]:
    for y in [9,10,11]:
        print(x*y) # 10, 11, 18, 20, 22, 27, 30, 33


# `for` loops can be combined with conditional based flow control
for x in range(0,25):
    if (x % 5 == 0):
        print(x) # 0, 5, 10, 15, 20


# A common task is to iterate over a list and use both the index and the value
# You can use `enumerate()` for this

for rank, flavor in enumerate(bagel_flavors):
    print(rank)
    print(flavor)

# "List comprehension" provides a concise syntax for creating a list by iterating over an existing list
# and applying some operation to each item

# Consider the case where we want a list of all the squared integers from 0 to 4.

# The "normal" way would be:
squares = []
for x in range(4):
    squares.append(x**2)
print(squares) # [0, 1, 4, 9]

# Here's how that would work using list comprehension syntax:
squares = [ x**2 for x in range(4) ]
print(squares) # [0, 1, 4, 9]

# A list comprehension consists of brackets containing an expression followed by a for clause, 
# then zero or more `for` or `if` clauses. The result will be a new list resulting from 
# evaluating the expression in the context of the `for` and `if` clauses which follow it.

# Here's another example, this one uses the `if` clause

numbers = [ 1, 33, 100, 2, 5, 3, 2, 7, 88, 19, 14, 81, 16, 16, 17, 17, 10011 ]
# just odd numbers
odds = [ x for x in numbers if x % 2 == 1]
print(odds) # [1, 33, 5, 3, 7, 19, 81, 17, 17, 10011]

# What happens if we iterate over a dict?

a = {'one': 1, "two": 2, "three": "foo"}

# This gives the keys of the dictionary
for x in a:
    print("Guess what...")
    print(x) # one, two, three

# It's the same as doing:
for key in a.keys():
    print("Good guess!")
    print(key) # one, two, three

# To iterate over the values in the dictionary:
for val in a.values():
    print("What we got?")
    print(val) # 1, 2, foo

# Here's another (and arguably better) way of iterating over a dict:
for key, value in a.items():
    print("Iterating...")
    print(key)
    print(value)

# As foreshadowed in the Lists and Dictionaries lesson, this is how you can check 
# if a dict contains a particular value and get the associated key
search_value = "foo"
for key, value in a.items():
    if value == search_value:
        print("Found search value, here's the key:")
        print(key)