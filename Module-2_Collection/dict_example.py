mydict={"id":1,"name":"nirav","sub":"python"}


#print(mydict)
#print(mydict["name"])
#print(mydict.get("sub"))


#mydict["name"]="Ashok"
#print(mydict)

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""

print(mydict)
print(mydict.keys())
print(mydict.values())

"""if "nirav" in mydict.values():
    print("Yes...")
else:
    print("Noo...Try again!")"""

#print(len(mydict))

#mydict["city"]="Rajkot"

#mydict.pop("id")
#del mydict["name"]
#mydict.clear()
#print(mydict)

newdict=mydict.copy()
print(newdict)