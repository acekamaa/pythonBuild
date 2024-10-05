#sets are unchangeable, unordered and unindexed.
fruitset = {"apple", "banana", "cherry"}
print(fruitset)

'''
Sets dont allow duplicates. 
True and 1 are considered the same type thus duplicates
only one value of the duplicates will be printed
'''
thiset = {"apple", "banana", 1, 2}
print(thiset)

#length of a set
print("Length of fruitset")
print(len(fruitset))

print("Length of thiset")
print(len(thiset))

#using the set constructor
#use two pairs of normal brackets
nameset = set(("allan", "kevin", "alvin"))
print(nameset)