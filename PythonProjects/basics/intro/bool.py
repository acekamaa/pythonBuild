class myclass():
    def __len__(self):
        return 0 #return 0 will give false return 1 true
    
myobj = myclass()
print(bool(myobj))

#isinstance() checks object to be of a certain datatype
x = 200
print(isinstance(x, int))