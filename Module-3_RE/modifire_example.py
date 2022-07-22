import re

mystr="This is Python Pyhhon RE! 8978"

#x=re.findall("[A-Z]",mystr)
#x=re.findall("[a-z]",mystr)
#x=re.findall("[A-Za-z]",mystr)
#x=re.findall("[0-9]",mystr)
#x=re.findall("[A-Za-z0-9]",mystr)

#-----------------------------------#

#x=re.findall("^This",mystr)
#x=re.findall("79$",mystr)
#x=re.findall("^[A-Z]",mystr)
#x=re.findall("[^A-Z]",mystr)


#-----------------------------------#

#x=re.findall("\w",mystr)
#x=re.findall("\W",mystr)
#x=re.findall("\d",mystr)
#x=re.findall("\D",mystr)
#x=re.findall("\AT",mystr)
#x=re.findall("78\Z",mystr)
#x=re.findall(r"\bThis",mystr)
#x=re.findall("\B78",mystr)

#-----------------------------------#

#x=re.findall("Py..on",mystr)

x=re.findall("This|That",mystr)
print(x)