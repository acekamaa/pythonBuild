def myfunc():
    #global keyword makes the variable x a global scope
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)