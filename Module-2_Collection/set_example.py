from hashlib import new


myset={'A','B','C','D','E','F'}

#print(myset)

#print(len(myset))

"""if "C" in myset:
    print("Yes...")
else:
    print("No..")"""

"""for i in myset:
    print(i)"""

#myset.add("G")
#myset.update(['G','H','I','J','A','B','E'])
#myset.remove('D')
#myset.pop()
#myset.clear()
#myset.remove('X')
#myset.discard('X')
#print(myset)


newset={'P','Q','R','S','A','C','E'}
#x=myset.union(newset)
x=myset.intersection(newset)
print(x)