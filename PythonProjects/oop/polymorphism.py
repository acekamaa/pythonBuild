# using len() in different ways
# len() in a string
s = "hello"
print(len(s))  # 5

# len() in a list
l = [1, 2, 3, 4, 5]
print(len(l))  # 5

# len() in a dictionary
d = {"a": 1, "b": 2, "c": 3}
print(len(d))  # 3

#use of len() in a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Ibiza")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()