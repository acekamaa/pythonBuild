#tuples are unchangeable(you cant change, add or remove items once created)
#but there are some work arounds - cnvert the tuple to a list, change the list and convert back to a tuple
x = ("apple", "banana", "cherry")
y = list(x) #tuple to list
y[1] = "kiwi"#change list
x = tuple(y)#list to tuple
print(x)

#add items
w = ("spinach", "carrots", "tomatoes")
r = list(w)
r.append("cabbage")
w = tuple(r)
print(w)

#add tuple to a tuple
'''
create a new tuple with the items and add it to the existing tuple
'''
print(x)#prints existing tuple
h = ("orange",)
x += h #add new tuple to the existing
print(x)

#remove items
'''
convert tuple to list, remove item convert it back to tuple
'''
t = list(x)
t.remove("apple")
x = tuple(t)
print(x)

#delete tuple completely
'''
del x - deletes the tuple
print(x) - generates an error as the tuple does exist, has been deleted
'''