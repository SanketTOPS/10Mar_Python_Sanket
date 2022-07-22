import re

mystr="Hello Hello Python!"

x=re.search("Hello",mystr)
y=re.findall("Hello",mystr)

print(x)
print(y)