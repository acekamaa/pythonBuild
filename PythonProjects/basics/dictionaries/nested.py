#nested dictionaries - dictionaries within a dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

'''
alternatively
add three dict into one

child1 = {
    "name": "Emil",
    "year": 2004   
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
'''

#access items use name of dict starting with the outer
print(myfamily["child2"]["name"])

#loop thru items - items()
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])