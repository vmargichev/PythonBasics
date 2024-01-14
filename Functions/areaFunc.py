def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
axe_length = 0.5
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
axe_area = area_of_circle(axe_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Axe length:", axe_length, "meters.")
print("Axe attack area:", axe_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")


# FUNCTIONS
# Functions allow us to reuse and organize code. For example, say we've written some code that calculates the area of a circle:

# radius = 5
# area = 3.14 * radius * radius
# Copy icon
# This works great! The problem arises when we want to calculate the area of more circles, each with its own radius. We could just copy the code and change the variable names like this:

# radius = 5
# area1 = 3.14 * radius * radius

# radius2 = 7
# area2 = 3.14 * radius2 * radius2

# radius3 = 11
# area3 = 3.14 * radius3 * radius3
# Copy icon
# But don't we want to reuse the same code? Why would we want to repeat our work? Instead, we can declare a new function, let's call it area_of_circle. Notice that the def keyword is written before the function name, and tells the Python interpreter that we're defining a new function.

# def area_of_circle(r):
#     pi = 3.14
#     return pi * r * r
# Copy icon
# The area_of_circle function takes one input (which can also be called a "parameter" or "argument") and returns one output. The body of the function is indented and contains the code that will be executed when the function is called. The return keyword tells the function to return the value of the expression that follows it.

# To use or "call" this function we can now pass in any number as the input (in this case, the radius), and capture the output into a new variable:

# radius = 5
# area = area_of_circle(radius)
# print(area)
# # 78.5
# Copy icon
# Here's a full example:

# def area_of_circle(r):
#     pi = 3.14
#     return pi * r * r

# radius = 5
# area = area_of_circle(radius)
# print(area)
# # 78.5

# radius = 6
# area = area_of_circle(radius)
# print(area)
# # 113.04
# Copy icon
# Here's a step-by-step explanation of what happens when the above code is executed:

# Line of Code	Explanation
# radius = 5	A new variable called radius is created and set to the value 5
# area_of_circle(radius)	The area_of_circle function is called with radius (in this case 5) as the input. Execution jumps to the function definition.
# def area_of_circle(r):	The input (5 in this case), is stored in a variable called r
# pi = 3.14	A new variable called pi is created with a value of 3.14
# 3.14 * r * r	A mathematical expression is evaluated, in this case 3.14 * 5 * 5
# return 3.14 * r * r	The result of the expression is returned from the function as its output
# area = area_of_circle(radius)	The returned value is stored in a new variable called area (in this case 78.5)
# print(area)	The value of area is printed to the console
# radius = 6	The radius variable's value is overwritten to now be 6
# area_of_circle(radius)	The area_of_circle function is called again, this time with radius (6) as the input. Execution jumps to the function definition.
# def area_of_circle(r):	The input (6 in this case), is stored in a variable called r
# pi = 3.14	A new variable called pi is created with a value of 3.14
# 3.14 * r * r	A mathematical expression is evaluated, in this case 3.14 * 6 * 6
# return 3.14 * r * r	The result of the expression is returned from the function as its output
# area = area_of_circle(radius)	The variable area is overwritten with the returned value (in this case 113.04)
# print(area)	The value of area is printed to the console
# Take some time to read through all the steps! It might take a few reads to fully understand what's going on, that's okay!

# ASSIGNMENT
# We need to calculate the size of a weapon's "attack area". With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

# Fix the bug on lines 14 and 15.

# The axe_area and spear_area variables should be set to the correct values instead of 0. You'll need to use the axe_length and spear_length variables.