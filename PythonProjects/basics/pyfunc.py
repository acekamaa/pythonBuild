#functions definitions start with keyword 'def'
def my_func():
    print("Hello, passing greetings from my_func")

#calling my_func
my_func()

#my_function args
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#arbitrary arguments - *args
def my_funci(*kids):
    print("The youngest child is " + kids[2])

my_funci("Emil", "Tobias", "Linus")

#sending arguments with key = value syntax -> keyword arguments (**kwargs)
#kwargs are used when the number of keyword arguments is unknown
#func will receive a dict of arguments and access the items 
def key_func(child3, child2, child1):
    print("The youngest child is " + child3)

key_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#use of **kwargs
def use_kwargs(**kid):
    print("His last name is " + kid["lname"])

use_kwargs(fname = "tobias", lname = "Refsnes")

#passing a list as an argument
def foodie(food):
    print("This are elements of func foodie:")
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

foodie(fruits)

#the pass statement - to avoid generating errors
def pfunc():
    pass

#positional-only arguments -> use '/' after the arguments
def pos_func(x, /):
    print(x)

pos_func(3)

#keyword only args -> add * before the args
def kwonly(*, x):
    print(x)

kwonly(x = 5)

#combine both positional-only and keyword-only
#args before /, -> positional-only and args after *, -> keyword only
def pos_kw_func(a, b, /, *, c, d):
    print(a + b + c + d)

pos_kw_func(5, 6, c = 7, d = 8)

#recursion  - calls itself
def tri_recursion(k):
    """Fuction describing the use of recursion in python."""
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
        return result
    return k
    
    print("Recursion Example Results:")
    tri_recursion(6)