'''
there are several ways to join sets:
union() && update() - joins all items and exclude duplicates
intersection() - keeps only the duplicates
difference() - retains unique items from 1st set
symmetric_difference() - keeps all items except the duplicates
'''

#union()
#you can also use the '|' operator and achieve the same results. but for sets with sets only
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

#join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#use update - changes the original set and doesn't return a new one
seta = {"a", "b", "c"}
setb = {1, 2, 3}
seta.update(set2)
print(seta)#gets all from setb and adds them to seta

#intersection - keeps only duplicates
#use & and achieve the same result but used between sets only
#intersection_update - changes the original set instead of returning a new one
thiset = {"google, microsoft", "apple"}
fruits = {"apple", "banana", "cherry"}

setf = thiset.intersection(fruits)
print(setf)

set5 = thiset & fruits
print(set5)

thiset.intersection_update(fruits)
print(thiset)

#use true, false and 0,1 and see the duplicates
mixset = {"apple", 1, "banana", 0, "cherry"}
anotherset = {False, "google", "apple", 2, True}

finset = mixset.intersection(anotherset)
print(finset)

#difference() - returns new set with unique items from set 1 that are not in the second set
#you can use the '-' operator to achieve the same result but only with sets
fruty = {"apple", "banana", "cherry"}
compny = {"google", "microsoft", "apple"}

retset = fruty.difference(compny)
print(compny)

returset = fruty - compny
print(returset)

#difference_update keeps the items that are not present in both sets
print(fruty)
print(compny)

''''
fruty.difference_udate(compnty)
print(fruty)
'''

#symmetric_difference() keeps elements not present in both sets
#use '^' operator for the same result
myupdate = fruty.symmetric_difference(compny)
print(myupdate)

uptodate = fruty ^ compny
print(uptodate)

#symmetric_difference_update() - keeps all but duplicates, changes the original set
print(fruty)
print(compny)

fruty.symmetric_difference_update(compny)
print(fruty)