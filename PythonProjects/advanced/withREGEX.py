import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x) # returns a match object