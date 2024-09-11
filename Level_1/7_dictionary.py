customer = {
    "name" : "john",
    "age" : 30,
    "is_verified" : True,
    "values": [1,2,3,4,5],
    "address" : {
        "street1" : "123 numpy street",
        "city" : "Huntsville"
    }
}

print(customer["name"])
customer["name"] = "KK"
print(customer)

# print(customer["first_name"]) # throws key error

print(customer.get("first_name")) # returns None

# return 'Augustin' if None, key not added to dictionary
print(customer.get("first_name", "Augustin" ))
print(customer.get("first_name"))


