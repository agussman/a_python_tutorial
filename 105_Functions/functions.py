# Functions are pieces of code used to perform a particular task.
# It allows you to isolate the code/logic of the function from the code calling the function. This typically makes the code calling the function easier to follow,
# either by masking the complexity of the function and/or avoiding repetitive code blocks.

# Breaking your program into functions has a lot of benefits, including improving readability, comprehension, testability, and sharing code

# A good rule of thumb is that if your program is doing something more than twice, you should probably be using a function.

# A better rule of thumb is that what you're doing is complex or fiddly, check to see if someone already wrote a function to do it. 
# We'll come back to this concept in the section on Modules.

# TODO: variable scoping


# Here's how you create a function in Python:
def are_valid_triangle_side_lengths(a, b, c):
    '''Test if the provided lengths could form the sides of a triangle'''
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

# `def` starts the definition of the function. 
# It's followed by the name of the function (`are_valid_triangle_side_lengths`)
# This particular function takes in three parameters (a,b,c), contained in `( )`, followed with a `:`.
# A function doesn't have to take parameters, but you still need the `()`.
# 
# It's good practice to name your function something descriptive and to include a comment
# to explain what the function is doing.
#
# The logic of the function is contained within the code block of the function.
# This particular function returns a value (either `True` or `False`) but a function doesn't have return anything.
# The `return` keyword denotes the value to be returned.

# Here's some examples of calling the function
a = 3
b = 4
c = 5
is_triangle = are_valid_triangle_side_lengths(a, b, c)
print(is_triangle) # True

x = 2
y = 3
z = 6

if ( are_valid_triangle_side_lengths(x,y,z) ):
    print("All good.")
else:
    print("Not a triangle.") # <-- This is printed

# You may have noticed that when we call `print()`, it looks an awful lot like calling a function
# This is because `print()` *is* a function. Look at you, you've been using functions since the beggining, aren't you awesome!

# Here's an example of a function that doesn't take in parameters or return any values

def say_something_nice():
    print("Something nice.")

say_something_nice() # Something nice.

# Functions can call other functions. Let's create another function to test if the sides of a triangle are a right triangle:
def is_right_triangle(a, b, c):
    '''Test if the provided lengths could form the sides of a right triangle'''

    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    else:
        return False

# Now we can combine them
def run_triangle_tests(a, b, c):
    '''Run triangle suitability tests on the provided side lengths'''

    if are_valid_triangle_side_lengths(a, b, c):
        print ("These are valid lengths for the sides of a triangle.")

        if is_right_triangle(a,b,c):
            print("\tThese could be the sides of a right triangle.")
        else:
            print("\tThis could not be a right triangle.")
        
    else:
        print("These are not valid lengths for the sides of a triangle.")


run_triangle_tests(a,b,c)

run_triangle_tests(x,y,z)

# Functions can also call themselves (this is called a "recursive function").
# The canonical example of this is the fibonacci numbers
# (but the most common use case is in whiteboard coding interviews ;-) )

def nth_fibonacci(n):
    '''Calculate the nth number in the Fibonacci sequence'''
    if (n < 1):
        print("Please enter a number greater or equal to 1")
    elif (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print(nth_fibonacci(9)) # 21

# TODO: scoping

# Variable scoping and passing variables to functions is a fairly complex subject. 

# Python isn't strictly "pass by reference" or "pass by value", it's "pass by assignment"
# (if the above doens't mean anything to you, that's fine)

# https://realpython.com/python-scope-legb-rule/ has more info

# Here we'll go over some practical situations you're likely to encounter.

# Basic types aren't modified in a function
def add_one(n):
    n = n + 1

x = 10
add_one(x)
print(x) # 10

# If you want the function to modify your input, return the value
def add_one_and_return(n):
    return n + 1

x = 20
x = add_one_and_return(x)
print(x) # 21


# Variables declared "outside" of a function scope are available inside the function
my_global_var = 7
def add_my_global_var(n):
    return n + my_global_var

x = 30
x = add_my_global_var(x)
print(x) # 37

# But, weirdly, this won't work:
def modify_and_add_my_global_var(n):
    # Throws "UnboundLocalError: local variable 'my_global_var' referenced before assignment"
    my_global_var = my_global_var + 1 # you can't do this
    return n + my_global_var

#x = 40
#x = modify_and_add_my_global_var(x)
#print(x)

# To modify the global variable, you need to specify global
# (note: this is not really recommended)
def global_modify_and_add_my_global_var(n):
    global my_global_var
    my_global_var = my_global_var + 1
    return n + my_global_var

my_global_var = 3
x = 50
x = global_modify_and_add_my_global_var(x)
print(my_global_var) # 4
print(x) # 54

# Here's a better way to do it, without relying on globals, assuming you actually want to modify two variables
def modify_two_variables(n, i):
    i = i + 1
    n = n + i
    return n, i

# Functions can return multiple values!
x = 60
y = 5
x, y = modify_two_variables(x,y)
print(x) # 66
print(y) # 6


# Note that all of the above applies to `int`, `float`, and `str`
# dicts and lists 

def modify_a_list(l):
    l.append(99)

my_list = [1,2,3]
modify_a_list(my_list)
print(my_list) # [1, 2, 3, 99]

def modify_a_dict(d):
    d["new"] = 99

my_dict = {"one": 1, "two": 2}
modify_a_dict(my_dict)
print(my_dict) # {'one': 1, 'two': 2, 'new': 99}

# Python 3.5 introduced "type hints"
# Type hints are used to denote the expected types of inputs and outputs to a function. They are useful to prevent you from shooting yourself in the foot
# by accidentally sending the wrong type into a function (e.g., passing in a string instead of an int).
# While they're optional and not super common, they look pretty wild I wanted to introduce them so you're not thrown if 
# you encounter one in the wild

def normal_function(score, name):
    if (score >= 10):
        print("Congratulations " + name)
        return True
    else:
        return False

# would become
def typehint_function(score: int, name: str) -> bool:
    if (score >= 10):
        print("Congratulations " + name)
        return True
    else:
        return False

# If you start your python journey by including type hints in all your functions, A+ Gold Star to you!


# Function annotations are added in the form `param_name : type` after each parameter in your function signature 
# and a return type is specified using the `-> type` notation before the ending function colon
# More: https://stackoverflow.com/a/32558710

# Python supports something called "function decorators".
# Their use and function is outside the scope of this tutorial, but I bring them up so you don't freak out
# if you see them (I think they look weird). Decorators are applied with the `@ ` above the function.
# Here `app.route()` is decorating the `index()` function
'''
@app.route('/')
def index():
    invoke_request_loggers(request)
    return 'Hello World!'
'''

# If you want to learn more this will get you started:
# [Primer on Function Dectorators in Python](https://realpython.com/primer-on-python-decorators/)