class Person:
    #The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, name, age):
        self.name = name
        self.age = age

#create object
p1 = Person("John", 36)

print(p1.name)
print(p1.age)