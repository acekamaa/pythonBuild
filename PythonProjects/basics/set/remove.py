#remove items using the remove() method
thiset = {"apple", "banana", "cherry"}
print(thiset)
thiset.remove("banana")
print(thiset)

#remove banana using discard()
thatset = {"watermelon", "orange", "banana"}
print(thatset)
thatset.discard("banana")
print(thatset)

'''
if the item to be removed is not in the set,
using remove() will raise an error
using discard() will not raise an error

using pop() removes a random item
'''

#remove a random item using pop() and return the value removed
vegeset = {"cabbage", "onions", "tomatoes", "carrots", "spinach"}
x = vegeset.pop()
print(x, " is the item removed from the set vegeset")

#clear() removes everything from the set
print(thiset)
thiset.clear()
print(thiset)

#del will delete the set completely
print(thatset)
del thatset
#print(thatset) will generate an error