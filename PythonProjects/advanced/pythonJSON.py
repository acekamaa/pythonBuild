import json

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
print(y["age"]) # result is a dictionary

# python to JSON
# create a Python object (a dictionary):
z = {
    "name": "Doe",
    "age": 22,
    "city": "Texas"
}   

# convert into JSON:
a = json.dumps(z, indent=4, sort_keys=True, separators=(".", "= "))
print(a) # result is a string

# convert python objects, print values
print(json.dumps(["apple", "banana", "cherry"]))
print(json.dumps(("apple", "banana", "cherry")))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))