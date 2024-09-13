from dns.dnssec import nsec3_hash


# this function can accept any number of arguments
# called unlimited arguments or unlimited positional arguments
def add(*args):
    print(type(args), args)
    # can also be accessed as positional argument
    print(f"arg[0] =  {args[0]}")
    running_sum = 0
    for arg in args:
        running_sum += int(arg)
    return running_sum


print(add(10, 20, 30, 40))

# not accurate
def calculate(**kwargs) -> int or float:
    print(type(kwargs), kwargs)
    running_val = 1
    for key, val in kwargs.items():
        # print(key, val)
        if key == "multiply":
            running_val *= val
        elif key == "divide":
            running_val /= val
        elif key == "add":
            running_val += val
        else:
            running_val -= val

    return running_val


print(calculate(add = 2, multiply = 3, divide = 1, subtract = 5))