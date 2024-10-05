#python doesnt have arrays, therefore use strings
#python doesnt have character datatype
#to access each character in a string, use square brackets and indexing as in arrays
a = "Hello, World!"
print(a[7])

#loop through the strings as in arrays
print("Looping through the string banana")
for x in "banana":
    print(x)
    
    #print length of string
    print(len(a))
    print(len(x))
    
    #check string using keyword "in"
    #check if "free" is present in the string
    txt = "The best things in life are free!"
    print("free" in txt)
    
    #use it in an if statement
    if "free" in txt:
        print("Yes, 'free' is present")
        
    #check if not present by using keyword "not in"
    print("expensive" not in txt)
    
    #only print if 'expensive' is NOT present
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")
        
    #slicing strings
    r = "Hello, welcome to my python learning platform"
    print(r[2:5])
    
    #slice from the start
    #leave the starting index blank
    print(r[:5])
    
    #slice to the end
    #leave out the ending index
    print(r[2:])
    
    #negative indexing
    #to start the slice from the end of the string
    print(r[-5:-2])