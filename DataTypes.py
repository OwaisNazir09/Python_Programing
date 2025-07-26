# =================== Python Data Types Tutorial ===================

# 1. Numeric Types

# Integer (int)
age = 25
print("Age:", age, "| Type:", type(age))

# Float (float)
price = 99.99
print("Price:", price, "| Type:", type(price))

# Complex (complex)
number = 3 + 4j
print("Complex Number:", number, "| Type:", type(number))


# 2. String (str)

# Text data
name = "Owais"
greeting = 'Hello, world!'
print("Name:", name, "| Type:", type(name))
print("Greeting:", greeting)


# 3. Boolean (bool)

# True or False values
is_student = True
has_access = False
print("Is Student:", is_student, "| Type:", type(is_student))


# 4. Sequence Types

# List (list) - ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "| Type:", type(fruits))
fruits.append("mango")  # Add new item
print("Updated Fruits:", fruits)

# Tuple (tuple) - ordered, unchangeable, allows duplicates
colors = ("red", "green", "blue")
print("Colors:", colors, "| Type:", type(colors))

# Range (range) - immutable sequence of numbers
nums = range(5)
print("Range object:", nums, "| Converted to list:", list(nums))


# 5. Mapping Type

# Dictionary (dict) - key-value pairs
person = {
    "name": "Owais",
    "age": 21,
    "is_student": True
}
print("Person Dictionary:", person, "| Type:", type(person))
print("Person's name:", person["name"])


# 6. Set Types

# Set (set) - unordered, no duplicates
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))

# Frozen Set (frozenset) - immutable set
frozen = frozenset([1, 2, 3, 2])
print("Frozen Set:", frozen, "| Type:", type(frozen))


# 7. None Type

# None (represents no value or null)
value = None
print("Value:", value, "| Type:", type(value))


# End of tutorial
print("\nAll basic Python data types demonstrated.")
