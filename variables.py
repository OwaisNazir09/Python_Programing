# ====================== Python Variables  =======================

# What is a variable?
# A variable is a container used to store data values.
# You can think of it like a label for a value in memory.

# Creating variables
name = "Owais"           # A string variable
age = 21                 # An integer variable
height = 5.9             # A float (decimal) variable
is_student = True        # A boolean variable (True or False)


# types of datatypes
# Numbers
age = 21             # int
pi = 3.14            # float

# Text
name = "Owais"       # str

# Boolean
is_student = True    # bool

# List
fruits = ["apple", "banana", "cherry"]  # list

# Tuple
coordinates = (10.5, 20.3)  # tuple

# Dictionary
person = {"name": "Owais", "age": 21}  # dict

# Set
unique_numbers = {1, 2, 3, 3}  # set

# None
data = None  # NoneType


# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student?", is_student)




# You can change the value of a variable
age = 22
print("Updated Age:", age)

# Variable naming rules:
# 1. Can contain letters, numbers, and underscores
# 2. Must start with a letter or underscore
# 3. Can't start with a number
# 4. Can't use spaces or special characters like @, $, %

# Valid variable names
user_name = "Ali"
_userAge = 25
roll_no123 = 45

# Invalid variable names (uncommenting these will cause errors)
# 123name = "Error"
# my name = "Error"
# user-name = "Error"

# Python is dynamically typed
# You don't need to declare the type; Python figures it out automatically

data = "Hello"
print(type(data))  # <class 'str'>

data = 100
print(type(data))  # <class 'int'>

# Multiple variable assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Assign the same value to multiple variables
a = b = c = "Python"
print(a, b, c)


#there is Something called global variables
# suppose we careted a varaible inside a function that gena.rally will local means taht we can us ethat only inside th function
# but we can use gloal keyword to make it accessbile fromm outside see 

def local_Variable():
    localvariable = 100
    global global_Variable
    global_Variable = 200
    print(local_Variable)

local_Variable()
# print(localvariable)
# NameError: name 'localvariable' is not defined. Did you mean: 'local_Variable'?
print(global_Variable)
# this global_Variable is working finw


# End of the basics
print("You just learned Python variables!")
