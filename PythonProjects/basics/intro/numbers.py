x = 4 #typeint
y = 12E4 #typefloat
a = 10.2 #typefloat
z = 3+5j #typecomplex
b = -5j #complex means has an imaginary rep by j

print(type(x))
print(type(y))
print(type(a))
print(type(z))
print(type(b))

"""
    type conversion
    you can't change from complex to another type
"""
#from int to float
c = float(x)
print(type(c))

#from float to int
d = int(y)
print(type(d))

#from int to complex
f = complex(x)
print(type(f))    