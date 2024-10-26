#pop() - removes items specified
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
thisdict.pop("model")
print(thisdict)

#popitem() - removes the last inserted item
thisdict.popitem()
print(thisdict)

#del - removes item with the specified key
thisdict["color"] = "red"
print(thisdict)

del thisdict["color"]
print(thisdict)

#the del can delete the entire dictionary
#del thisdict