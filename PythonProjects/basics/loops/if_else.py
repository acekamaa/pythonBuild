a = 33
b = 30

#short hand if
if a > b: print("a is greater than b")

#short hand if else
c = 20
d = 10

#print("C is greater than D") if c > d else print("D is greater than C")

#one line if else statement with 3 conditions
f = 330
g = 330

#short hand if else
# print("F is greater than G") if f > g else print("F == G") if f == g else print("G is greater than F")

#logical and
if a > b and c > d:
    print("Both conditions are true")

#logical or
if a > b or a > c:
    print("Atleast one of the conditions is True")
    
#negate
if not b > a:
    print("b is NOT greater than a")