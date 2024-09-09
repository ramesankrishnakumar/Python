
numbers = (1,2,3) # same as list but with ()
# tuples are immutable, so numbers[0] = 10 will throw an error

# unpacking

coordinates = (1,2,3)
# instead of coordinates[0] + coordinates[1] + ....
# does not work if there are more than  three values in the tuple
# variable count should be same as the number of elements
x, y, z = coordinates
print(x + y + z)