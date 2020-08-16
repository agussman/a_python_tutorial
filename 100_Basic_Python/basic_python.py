# Welcome to Python!

# Lines starting with # (pound/number sign/octothorpe) are comments and don't "do" anything

''' Three apostrophes can also start and end a comment '''

'''
This is good for

multiline

comments
'''

# As tradition dictates, we begin with:
print("Hello world!")

# the print function automatically adds a closing linebreak
print("Line 1")
print("Line 2")
print("line 3")

# You can directly insert your own linebreaks with \n
print("Line 4\nLine 5\nLine 6")

# You can directly insert your own tabs with \t
print("Hey you!\n\tLook over here!")

# In what is probably not a surprise to you, computers can do math

# They can also store the results of mathematical operations in a variable
x = 1 + 2
print("The next line will print the results of 1 + 2:")
print(x)

# Side note: In a lot of examples I'm using single-character variable names. You should probably
# not do that in any real code.

# What may be a surprise to you is that you don't need to declare the type of variable

a = 99
b = 77.77
c = "Dawg."

print(a) # 99
print(b) # 77.77
print(c) # Dawg.

# Oh yeah, comments can go at the end of lines, too

# Here's more math examples

a = 99 + 22 # Multiplication
b = 99 - 22 # Subtraction
c = 99 * 22 # Multiplication
d = 99 / 22 # Division

print(a) # 121
print(b) # 77
print(c) # 2178
print(d) # 4.5

# A couple of notes on the above:
# -- We initially assigned a string ('str') value to c (e.g., "Dawg."). Later, we assigned it an `int` (integer) value (e.g., 2178).
# -- If you got '4' instead of '4.5' for d, you are almost certainly running Python 2.

# You may find yourself needing to convert between different types of variables
# Let's create some sample variables:
a_string = "1"
an_integer = 1
a_float = 1.0

# You can check their type with the `type()` build-in function:
print(type(a_string)) # <class 'str'>
print(type(an_integer)) # <class 'int'>
print(type(a_float)) # <class 'float'>

# To convert from one data type to another, use the built-in functions `str()`, `int()`, and `float()`
# (This is also called "casting" a variable)
string_to_int = int(a_string)
string_to_float = float(a_string)
float_to_string = str(a_float)

print(string_to_int) # 1
print(string_to_float) # 1.0
print(float_to_string) # 1.0

print(type(string_to_int)) # <class 'int'>
print(type(string_to_float)) # <class 'float'>
print(type(float_to_string)) # <class 'str'>

# Note that (for obvious reasons?) the string actually has to be a number; these don't work:
# print(int("Zero"))
# print(float("Words"))


# Division in Python 3 always returns a float:
print(4 / 2) # 2.0
# If you want Python 2 style division aka "floor division" use //
print(4 // 2) # 2

# Here are some other operations it is sometimes useful to use
a += 1
b -= 1
print(a) # 122
print(b) # 76

# Sorry fans of unary increment and decrement operators, these are not a thing in Python:
# a++ # Nope
# b-- # Nope
# ++a # Also nope
# --b # Nice try, still nope

# Here are some other operations that you could use but probably won't
c *= 2 
d /= 2
print(c) # 4356
print(d) # 2.25
# Why not just write 
# c = c * 2

# Here is how you do exponents
e = 2**3 
print(e) # 8

# And here is good-ole modulo, which always makes me feel like a CS whiz whenever I have occassion to use:
m = 55 % 10
print(m) # 5



# You can also use variables on the right hand side of the equation
d = a * b - c
print(d) # 4916

# Generally in Python, if you create a variable based on another variable, then modify one of them, 
# the other is unchanged
a = 2
b = a
b = b - 3
print(a) # 2
print(b) # -1

# I say "Generally" because for dictionaries and lists (which we will come to later) this is not the case:
a = [0,2,3]
b = a
b.append(99)
print(a) # [0, 2, 3, 99]
print(b) # [0, 2, 3, 99]

a = {
    "one": 1,
    "two": 2
}
b = a
b["three"] = 3
print(a) # {'one': 1, 'two': 2, 'three': 3}
print(b) # {'one': 1, 'two': 2, 'three': 3}


# This isn't really a tradition, but it seems like it should be:
print("Goodbye world!")