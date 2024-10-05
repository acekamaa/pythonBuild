thistuple = ("apple","banana", "cherry")
for x in thistuple:
    print(x)
    
#using index numbers. use range() and len()
vegetuples = ("cabbage", "carrots", "cucumber")
for i in range(len(vegetuples)):
    print(vegetuples[i])
    
#using while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
    
#newtuple
meatuple = ("beef", "chicken", "pork")

#join tuples
tuple3 = thistuple + vegetuples + meatuple
print(tuple3)

#multiply tuples
tuple4 = meatuple * 2
print(tuple4)

#tuple methods
tuple1 = (1, 2, 5, 3, 4, 5, 6, 7, 5)
x = tuple1.index(5)
print(x)

z = tuple1.count(5)
print(z)