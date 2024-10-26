#copy() - makes a copy of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()
print(mydict)

#dict() - another way to make a copy
newdict = dict(thisdict)
print(newdict)