# Welcome to Python!

# Lines starting with # (pounnd/number sign/octothorpe) are comments and don't "do" anything

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

# You can roll your own linebreaks with \n
print("Line 4\nLine 5\nLine 6")

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

# A couple of notes on the above:
# We reused the variable c and switched it from being a `str` (string) to an `int` (integer).
# If you got '4' instead of '4.5' for d, you are almost certainly running Python 2.

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

# I say "Generally" because for dictionaries and lists (which we will come to later) this is not the case

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