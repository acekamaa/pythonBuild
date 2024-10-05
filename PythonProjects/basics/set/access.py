thiset = {"apple", "cherry", "banana"}

#check if item is present using 'in'
print("banana" in thiset)

#check if item is not present
print("cherry" not in thiset)

#add items - use add()
thiset = {"apple", "banana", "cherry"}
thiset.add("orange")
print(thiset)

#add sets - use update()
tropical = {"pineapple", "mango","papaya"}

thiset.update(tropical)
print(thiset)

#add any iterable
mylist = ["kiwi", "orange"]

thiset.update(mylist)
print(thiset)