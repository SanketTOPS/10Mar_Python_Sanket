try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
except Exception as e:
    print(e)
else:
    print("Sum:",a+b)
    print("This is Exception handling in Python!")