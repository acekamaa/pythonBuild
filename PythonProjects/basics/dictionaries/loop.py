#using for loop
thisdict = {"type": "fruit", "name": "apple"}

for x in thisdict:
    print(thisdict[x])

#values()
for x in thisdict.values():
    print(x)

#keys()
for x, y in thisdict.items():
    print(x, y)

#loop through keys n values using items()
for x, y in thisdict.items():
    print(x, y)