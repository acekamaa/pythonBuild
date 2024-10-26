#dict are objects according to python.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(type(thisdict))#prints <class 'dict'>

#get the value of an item using the key-name
print(thisdict)
x = thisdict["model"]
print(x)

#try the same using get
y = thisdict.get("year")
print(y)

#print the list of all keys
a = thisdict.keys()
print(a)

#using dict constructor
thedict = dict(name = "John", age = 36, country = "Norway")
print(thedict)