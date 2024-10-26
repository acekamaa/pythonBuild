#change values by referring to its key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#before change
print(thisdict)

#after change
thisdict["year"] = 2018
print(thisdict)

#update() - updates dictionary with the items from the given argument
thisdict.update({"year": 2020})
print(thisdict)