from functools import reduce

def add_1(x):
    return x + 1

add_1_lambda = lambda x: x + 1

print(f"add_1_lambda add 1 to 2: {add_1_lambda(2)}") # 3
print(f"add_1 add 1 to 2: {add_1(2)}") # 3

def square(x):
    return x ** 2

# list comprehension
list_of_nums = [item for item in range(1, 11)]

list_of_squares = list(map(square, list_of_nums))

list_of_squares_lambda = list(map(lambda x: x**2, list_of_nums))

list_filtered_lambda = list(filter(lambda x: x % 2 == 0, list_of_nums))

print(f"list_filtered_lambda: {list_filtered_lambda}")

# common use case of lambda

list_of_tuples = [
    (1, 'z', 'able'),
    (2, 'a', 'love'),
    (4, 'a', 'andrew'),
    (3, 'c', 'world')
]

sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1])
print(f"sorted_list_of_tuples: {sorted_list_of_tuples}")

sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1] + x[2])
print(f"sorted_list_of_tuples: {sorted_list_of_tuples}")


sum_of_list = reduce(lambda x, y: x + y, list_of_nums)
print(f"sum_of_list: {sum_of_list}")

max_value_list = reduce(lambda x, y: x if x>y else y, list_of_nums)
print(f"max_value_list: {max_value_list}")











