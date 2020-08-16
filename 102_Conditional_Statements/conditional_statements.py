# Use conditional statements to control the flow of your program

witch_weight = 110
duck_weight = 2

if witch_weight > duck_weight:
    print("The witch weighs more than the duck.")
print("Ni!")

# A couple of things here:

# * `if` is followed by a boolean expresison that evaluates to True or False
# 
# * Python doesn't use { and } for scoping, it uses indentation.
#   Your editor should just interpret a tab press as 4 spaces. If it doesn't, you should see if that's 
#   a setting you can change, or get a new editor.
#
# * Note the `: at the end of the line starting with `if`. It is important.
#
# * Parenthesis around the conditional statement aren't required, but don't hurt anything either
if (witch_weight > duck_weight):
    print("The witch still weighs more than the duck.")

# `if` can accept any conditional expression:
a = 3
b = 4
c = 5
if  (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, and c are valid lengths for the sides of a triangle.")

# use 'else' to do something else if the 'if' statement doesn't evaluate to True
a = 3
b = 4
c = -1
if  (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, and c are valid lengths for the sides of a triangle.")
else:
    print("a, b, and c are NOT valid lengths for the sides of a triangle.")


# Use 'elif' (aka "else if") when there are multiple conditions you want to check
a = 3
b = 4
c = 5
if (a**2 + b**2 == c**2):
    print("Valid lengths for a right triangle where the hypotenuse is c.")
elif (a**2 + c**2 == b**2):
    print("Valid lengths for a right triangle where the hypotenuse is b.")
elif (b**2 + c**2 == a**2):
    print("Valid lengths for a right triangle where the hypotenuse is a.")
else:
    print("Not valid lengths for a right triangle.")

# Occasionally you'll have a situation where you want to test for a condition but then not do amything.
# Because of Python's indentation based scoping, you can't just leave it empty:
#
# if (x < 1):
#     print("x is too small.")
# if (x == 1):
# if (x > 1):
#     print("x is too big.")
#
# The above causes python to freak out. 
#
# Instead, you can use the keyword 'pass'
x = 1
if (x < 1):
    print("x is too small.")
elif (x == 1):
    pass
elif (x > 1):
    print("x is too big.")

# Because it is very useful, you can also plug some other things into an if statement
# and it will behave in a mostly-sensible way:
x = 0
if (x):
    print("This won't execute")
else:
    print("0 evaluates to False")

x = 1
if (x):
    print("1 evaluates to True")
else:
    print("This won't execute.")

x = 99
if (x):
    print("Non-zero numbers evaluate to True")
else:
    print("This won't execute.")

x = -1
if (x):
    print("Non-zero numbers evaluate to True (even negative numbers)")
else:
    print("This won't execute.")

x = "text"
if (x):
    print("Non-empty strings evaluate to True")
else:
    print("This won't execute.")

x = ""
if (x):
    print("This won't execute.")
else:
     print("Empty strings evaluate to False")

x = "False"
if (x):
    print("Non-empty strings evaluate to True (I tried to trick you)")
else:
    print("This won't execute.")

x = None
if (x):
    print("This won't execute.")
else:
     print("None evaluates to False (but is not equal to False)")