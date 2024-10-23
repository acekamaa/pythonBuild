'''
contains the various methods found in the sets
add()
clear() - removes all elements
copy() - returns a copy of the set
difference() - returns a set containing the difference in two or more sets (shortcuts '-')
difference_update() - removes the items in this set that are also included in another, specified set (-=)
discard() - remove the specified item
intersection() - returns a set thats an intersection of two other sets (shortcut - '&')
intersection_update() - removes the items in this set that are not present in other specified sets (shortcuts &=)
isdisjoint() - returns whether two sets have an intersection or not
issubset() - returns whether another set contains this set or not (<=)
        - returns whether all items in this set is present in other specified sets(<)
isupperset() - returns whether this set contains another set or not(>=)
        - returns whether all items in other specified sets is present or not (>)
pop() - removes an element from the set
remove() - removes the specified element
symmetric_difference() - returns a set with the symmetric differences of two sets(^)
symmetric_difference_update() - inserts the symmetric differences frm this set and another (^=)
union() - return a set containing the union sets(|)
update() - update the set with the union of this set and others(|=)
'''

set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4}
set3 = {"apple", "banana", "cherry", "guava"}
set4 = {"pie", "cheese", "salad", "ham"}

#use the methods listed above
print(set1)
set1.add("e")
print(set1, " added letter \'e'")

print(set2)
set5 = set2.copy()
print(set5, " contains a copy of set2")

print(set3)
set6 = set3.difference(set1, set2)
print(set6)

