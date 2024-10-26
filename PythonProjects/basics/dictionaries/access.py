car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#print all the keys
x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x)#after change

#get the values
x = car.values()
print(x)

#get items - items() returns each item as tuples in a list
x = car.items()
print(x)
print("Dictionary items printed as tuples in a list")

#check if a key exists - 'in'
if "model" in car:
    print("Yes, \'model\' is one of the keys in the car dictionary")
