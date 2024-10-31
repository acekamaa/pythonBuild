for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    #the break can also come before the print as in
    #if x == "banana":
    #break
    #print(x)

matunda = ["apple", "banana", "cherry"]
for x in matunda:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

#add starting range(2, 6)
for x in range(2, 6):
    print(x)

#add increment factor
for x in range(2, 30, 3):
    print(x)

adj = ["red", "big", "tasty"]

for x in fruits:
    for y in adj:
        print(x, y)

'''
for loops cannot be empty but if yours is put a pass
to avoid errors
for x in [0, 1, 3]:
pass
'''