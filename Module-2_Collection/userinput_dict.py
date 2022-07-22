mydict={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    k=input("Enter your key:")
    v=input("Enter your value:")
    mydict[k]=v

print(mydict)
