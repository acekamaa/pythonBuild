#copy() used to copy lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)#prints a copy of thislist

#use list method
anotherlist = list(thislist)
print(anotherlist)#prints a copy of thislist

#using slice operator
newlist = thislist[:]
print(newlist)#also prints a copy of thislist

#you can append items from list2 to list1 and viceversa
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    
print(list1)

#or use extend() - adds elements from one list to another
list3 = ["wa", "we", "wi", "wo", "wu"]
list4 = ["ba", "be", "bi", "bo", "bu"]
list3.extend(list4)
print(list3)

#join three or more lists
list4 = list1 + list2 + list3
print(list4)