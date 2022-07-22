#myset={}

myset=set()

n=int(input("Enter number of set elements:"))

for i in range(n):
    el=input("Enter Set Element:")
    myset.add(el)


print(myset)