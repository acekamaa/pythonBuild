thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#sorts the list alphabetically

#sort the list numerically - ascending
nlist = [100, 50, 65, 82, 23]
nlist.sort()
print(nlist)

#sort the list in descending order
nlist.sort(reverse=True)
print(nlist)

#customize sort function
#returns a number that will be used to sort the list, lowest number first
def myfunc(n):
    return abs(n - 50)

nlist.sort(key = myfunc)
print(nlist)

#case sensitive sort
#items with upper case have a higher precedence than those in lowercase
newlist = ["banana", "Orange", "Kiwi", "cherry"]
newlist.sort()
print(newlist)

#using str.lower for case insensitive sort
newlist.sort(key = str.lower)
print(newlist)

#reverse order
newlist.reverse()
print(newlist)