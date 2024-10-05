fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#put all elements with "a" in the newlist
for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)

'''
syntax
    newlist = [expression for item in iterable if condition == True]

the return value is a new list, leaving the old list unchanged
'''

#only accept items that are not apple
#newlist = [x for x in fruits if x != "apple"]
#print(newlist)

#without using the if condition
#newlist = [x for x in fruits]

#use range to create an iterable
#newlist = [x for x in range(10)]

#print(newlist)

#lets add a condition
#newlist = [x for x in range(10) if x < 5]
#print(newlist)

#set items to upper
newlist = [x.upper() for x in fruits]
print(newlist)

#return the item if it is not banana if it is banana return orange instead
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)