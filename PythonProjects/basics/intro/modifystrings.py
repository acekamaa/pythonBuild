a = "Hello, world!"
#to upper()
print(a.upper())

#to lower()
print(a.lower())

#removes whitespace
b = " Hello, World! "
print(a.strip()) #prints "Hello, World!"

#replace string
print(a.replace("H", "J"))

#split string
#forms a list from where the separator has been specified
print(a.split(","))#returns ['Hello', 'World!']

#using fstrings
#placeholders - contain variables, operations, functions and modifiers
age = 36
me = f"My name is kvn, I am {age}"
print(me)

#using placeholders
price = 59
sales = f"The price is {price} dollars"
print(sales)

#lets format the placeholder with a modifier
#add a modifier by adding a colon followed by a legal formatting type
sales = f"The price is {price:.2f} dollars"
print(sales)

#python math operations
sales = f"The price is {20 * 3} dollars"
print(sales)