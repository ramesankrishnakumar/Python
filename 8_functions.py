# Pep8 python standard to require two line breaks between functions
# or else pycharm show suggestion
# "PEP8: expected 2 blank lines, found 1"
print("Begin execution")


def greet_user(name):
    print(f"Hello {name}")


greet_user("Bob")
print(greet_user("Bob")) # prints None, by default all function returns none,  similar to void or unit
print("End execution")

# no value passed for name, will throw an error
# greet_user()


def greet_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

# positional arguments "John" to first_name and
# "Doe" to last_name
greet_full_name("John", "Doe")

# or use have keyword arguments
greet_full_name(last_name="Smith", first_name="John")

# function returning a value
def square(number):
    return number * number

squared_value = square(10)
print(squared_value) # or print(square(10))