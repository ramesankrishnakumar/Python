temperature = 5

if temperature > 30:  # in python we don't have curly braces
    print("It's a hot day")
    print("drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a cold day")
else:
    print("It's freezing")


weight = float(input("What is your weight? "))
unit = input("(K)g or (L)bs?").upper()

if unit == "K":
    converted_weight = weight * 2.2
    print(f"weight in Lbs: {converted_weight}")
else:
    converted_weight = weight / 2.2
    print(f"weight in Kg: {converted_weight}")


