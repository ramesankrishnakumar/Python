# age = int(input("Enter your age: "))
# print(age)
# if the user enters a str value, program with fail


try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:   # catch
    print("Invalid input")

