# A Boolean value is either True or False. A Boolean expression returns a Boolean value-- True or False

# In Python, we can test if two values are equal with ==
print(3 == 3) # True
print(3 == 4) # False

# And if we want to test if things are not equal, we use !=
print(3 != 3) # False
print(3 != 4) # True

# In the above, == and != are boolean operators that return boolean values (true or false)

# You can also do your standard numerical comparison operators
print(3 > 4) # False
print(3 < 4) # True
print(4 >= 3) # True
print(4 <= 3) # False

# All of the above also work with variables
a = 3
b = 4
print( a == a ) # True
print( b < a )  # False
# At some point you will introduce a bug into your program because you mixed up = and ==.
# This is just one of those things that happens to everybody sooner or later.

# You can also use Strings
t = "text"
print( t == t ) # True
print( t == "text" ) # True

# On strings the comparison operators test lexical order
print( "apple" < "banana") # True
print( "apple" < "apple tree") # True
print( "one" < "four") # False, because strings

# The below is a no-go, it doesn't know how to compare a string to an int
# print( t < 1) # fails with TypeError
# print( "one" < 1) # I like the way you think, but still a TypeError

# You can also assign Boolean values directly, or test them directly
a = True
print(a == True) # True
b = False
print(b == False) # True!

# You can also use 'and' and 'or' operators:
a = 3
b = 4
c = 5
print( (a < b) and (b < c) ) # True
print( (a < b) and (c < a) ) # False

print( (a < b) or (b < c) ) # True
print( (a < b) or (c < a) ) # True
print( (b < a) or (c < a) ) # False

# Are these valid lengths for the sides of a triangle?
print(  (a + b > c) and (a + c > b) and (b + c > a) ) # True

# Are these valid lengths for a right triangle?
print(  (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2) ) # True

# There's also a 'not' operator
print( (a < b) and not (b < c) ) # False
print( (a < b) and not (c < a) ) # True
print( not (a < b) and (b < c) ) # False

# Order of operations is not, and, or
print( not (a < b) and (c < a) ) # False
print( not ((a < b) and (c < a)) ) # True