thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
#loop through the index numbers
for i in range(len(thislist)):
    print(thislist[i])
    
#using a while loop
thelist = ["mango", "avocado", "peach"]
i = 0
while i < len(thelist):
    print(thelist[i])
    i = i + 1
    
#looping using list comprehension
#short hand for loop
[print(x) for x in thelist]