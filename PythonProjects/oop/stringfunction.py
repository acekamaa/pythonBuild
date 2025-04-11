# representing the class object as a string
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1) 

class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

    def myfunc(self):
        print("Hello my name is " + self.name + " age: " + str(self.age) + " graduated year: " + str(self.year))

p1 = Student("Peter", 20, 2022)
p1.myfunc() # object method from parent class