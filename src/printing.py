"""
Python provides a number of ways to perform printing. Research
how to print using the:
printf operator, 
the `format` string method, 
and by using f-strings.

"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("%s" % z, "%i" % x, "%d" % y)
# print("%2i, %4.2f, %15s" % (x, y, z))

# Use the 'format' string method to print the same thing

print('{} {} {:.2}'.format(z,x,y))
# Finally, print the same thing using an f-string


# I would add that since version 3.6, we can use fstrings like the following

#personal example:

# foo = "john"
# bar = "smith"
# print(f"My name is {foo} {bar}")

print(f'This is what it reads: {z} {x} {y}')