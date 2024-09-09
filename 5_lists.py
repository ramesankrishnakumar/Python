names = ["john", "bob", "sam", "tiger", "peach", "snow", "candy", "bubbles"]
print(names[0]) # first
print(names[-1]) # last
print(names[-2]) # last but one

# updating a list element
names[0] = 'jon'

# printing a range of elements, returns a new list does not modify the original
# ['jon', 'bob', 'sam']
print(names[0:3])

# same ['jon', 'bob', 'sam']
print(names[:3])

# every second element
# ['jon', 'sam', 'peach', 'candy']
print(names[::2])
# every second element from reverse
# ['bubbles', 'snow', 'tiger', 'bob']
print(names[::-2])

# every second element starting from index 1
# ['bob', 'tiger', 'snow', 'bubbles']
print(names[1::2])


# List methods

nums = [1,2,3,4,5,6,7,8,9,10]
# insert at the end
nums.append(11)
print(nums)

# insert at a specific position
# insert at the beginning
nums.insert(0,-10)
print(nums)

# remove a value from list
# throws error if the element is not present
nums.remove(-10)
print(nums)

# does a number exists in nums
print(1 in nums) # prints True

# size of the list
print(f"size of list {len(nums)}")

# clear the list
nums.clear()
print(nums)

# 2D lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] = 20
print(matrix[0][1]) # prints 20

for row in matrix:
    for item in row:
        print(item)




