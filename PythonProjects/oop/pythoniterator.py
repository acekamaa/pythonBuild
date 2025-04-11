# using iter() on a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

# printing the items
print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry
# print(next(myit))  # raises StopIteration exception

# using iter() on a string
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # b
print(next(myit))  # a
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# you can iterate using for
for x in mystr:
    print(x)