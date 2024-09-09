"""
this is a block comment
"""
# this is a line comment

# dynamic types in python
age = 20

# dynamic string
print(f"Hello World: {age}")

age = 30
print(f"Hello World: {age}")

# python variable names use snake case
first_name = "John" # OR first_name = 'John'
is_online = False # boolean is True & False not true & false

# getting user input

name = input("What is your name? ")

print(f"Hello {first_name}, welcome to Python {name}")

# OR use string concatenation

print("Hello " + first_name + ", welcome to Python " + name)

# Type casting

birth_year = input("What is your birth year? ")
# age = 2024 - birth_year # this will throw error that '-' is not supported for int and str
age = 2024 - int(birth_year)
print(f"You are {age} years old")

# similarly
# float(variable) for converting to float
# bool(variable) for converting to boolean
# str(variable) for converting to string

# exercise addition between floating point and integer

num_1 = float(input("What is your first number? "))
num_2 = float(input("What is your second number? "))
result = num_1 + num_2
print(f"Your result is {result}")












