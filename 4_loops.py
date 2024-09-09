# while loops

i = 1 # initial value

while i <= 5:
    print(i)
    i += 1 # increment value of i , omitting this will give an infinite loop
    
i = 1
while i <= 5:
    print(i * '*')
    i +=  1

# foreach loop

numbers = [1,2,3,4,5,6]
for item in numbers:
    print(f"item: {item}")

i = 0
while i < len(numbers):
    print(f"number: {numbers[i]}")
    i += 1

# Range
numbers = range(1, 100, 2) # range from 1 to 100 with 2 as step
for item in numbers:
    print(f"range_item: {item}")

# or better we can use directly in for

for item in range(1, 100, 2):
    print(f"range_item: {item}")

