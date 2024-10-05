#use add() 
thiset = {"apple", "banana", "cherry"}
thiset.add("orange")
print(thiset)

#add items from another set, use update()
print(thiset)
tropical = {"pineapple", "papaya", "mango"}

thiset.update(tropical)
print(thiset)

'''
the object in the update doesnt have to be a set, can be any other iterable
'''
print(thiset)
mylist = ["kiwi", "strawberry"]

thiset.update(mylist)
print(thiset)