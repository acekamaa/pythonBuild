#small anonymous function that can take any number of args but with one expression.
#add 10 to arg a and return the result
x = lambda a : a + 10
print(x(5))

#multiply a and b and get the result
x = lambda a, b : a * b
print(x(5, 6))

#use lambda inside a func
def myfunc(n):
    return lambda a : a * n

#lambda func that doubles arg input
mydoubler = myfunc(2)

print(mydoubler(11))