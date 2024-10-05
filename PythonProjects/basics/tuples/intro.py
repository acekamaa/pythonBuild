#ordered, allow duplicates and unchangeable
#items cannot be removed once a tuple has been created
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#print tuple length
print(len(thistuple))

#tuple of one item - must add ','
thattuple  = ("apple",)
print(type(thattuple))
print(thattuple)

#tuples can hold multiple datatypes at the same time
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))
print(tuple1)

#tuple() constructor
#uses double round brackets
antuple = tuple(("baseball", "cricket", "softball"))
print(antuple)

#access an item referring to index
#use square brackets
print(antuple[1])

#negative indexing
print(antuple[-1])

#range of index
print(tuple1[2:5])

#check if item exists
if "male" in tuple1:
    print("Yes, male is part of my tuple")