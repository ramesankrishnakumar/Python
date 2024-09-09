print(10 / 3 )  # 3.33
print(10 + 3 )  # 13
print(10 - 3 )  # 7
print(10 * 3 )  # 30
print(10 % 3)   # remainder 1
print(10 ** 3)  # 10 ^ 3

# now something new
print(10 // 3)  # integer division returns 3
i = '*'
i = i * 10
print(i)  # prints i ('*') 10 times
# end

x = 10
x += 3  # x = x + 3
print(f"x = x + 3: {x}")
x -= 3
print(f"x = x - 3: {x}")
x *= 3
print(f"x = x * 3: {x}")
x /= 3
print(f"x = x / 3: {x}")

# operator precedence

x = x + 3 * 2  # 16.0

# same brackets to change the operator precedence
x = 10
x = (x + 3) * 2 # 26

# comparisons

x = 3 > 2 # boolean operation returning **True**

print(f"x = {x}")

x = 3 < 2 # **False**

x = 3 >= 2 # True

x = 3 <= 2 # False

x = 3 == 2 # False

x = 3 != 2 # True


# Logical operations

price = 20

print( price > 10 and price < 30)
print(10 < price < 30)  # prints true and readable

print(price < 100 or price > 20) # true

print(not price > 10) # false









