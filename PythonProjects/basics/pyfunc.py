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

#sending arguments with key = value syntax
def key_func(child3, child2, child1):
    print("The youngest child is " + child3)

key_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")