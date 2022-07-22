fl=open("userdata.txt","a")

id=input("Enter ID:")
name=input("Enter Name:")

fl.write(f"\nID:{id}\n")
fl.write(f"Name:{name}\n")
fl.write(f"------------------\n")