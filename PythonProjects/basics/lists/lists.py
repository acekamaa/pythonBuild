thislist = ["apple", "banana", "cherry"] #lists are ordered, changeable and can have duplicates as each item is accessed through indexes
print(thislist[1])

#negative indexing
#-1 refers to the last item and -2 refers to the second last item
print(thislist[-1])

#range of indexing
print(thislist[1:])

#new list
thelist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#doesnt include the -1 index
print(thelist[-4:-1])

#check if item exists
if "apple" in thelist:
    print("Yes, \'apple\' is in the fruits list")
    
#changing item value
thislist[1] = "blackcurrent"
print(thislist)

#change a range of item values
thelist[0:2] = ["blackcurrent", "watermelon"]
print(thislist)

#you can insert an item at a specified index. Use insert()
thislist.insert(2, "pineapple")
print(thislist)

#add at end of the list. use append()
thislist.append("orange")
print(thislist)
print(len(thislist))

#add elements from another list/set/dict/tuple. use extend()
tropical = ["papaya", "peach", "guacamoli"]
thislist.extend(tropical)
print(thislist)
print(len(thislist))

#remove cherry
thislist.remove("cherry")
print(thislist)

#remove at specified index. use pop() or del
#failure to specify the index, removes the last item
thislist.pop(1)
print(thislist)

#use del with index
del thislist[2]
print(thislist)#removes orange

#use del without the index. Removes everything in the entire list
#del thislist

#clear empties the list
thislist.clear()
print(thislist)