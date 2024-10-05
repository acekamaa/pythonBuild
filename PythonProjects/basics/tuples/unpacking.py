#assingin values tuple is packing
#extracting values back into variables - unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #unpacking

print(green)
print(yellow)
print(red)

#unpacking using asterisk
'''
if number is less than the number of values, add * to the variable name
and the values will be assigned to it as a list
'''
matunda = ("apple", "cherry", "banana", "strawberry", "rasberry")

(first, second, *third) = matunda

print(first)
print(second)
print(third)

#when the *var isnt the last in the list
(one, *two, three) = matunda

print("the second variable has the asterisk")
print(one)
print(two)
print(three)