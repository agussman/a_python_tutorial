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