fl=open("userdata.txt","r")

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[5])

n=1
for i in fl:
    print(i)
    print(f"Line={n} = {len(i)}")
    n+=1