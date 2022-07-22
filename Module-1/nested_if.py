sub1=int(input("Enter Subject1 Mark:"))
sub2=int(input("Enter Subject2 Mark:"))
sub3=int(input("Enter Subject3 Mark:"))

# ---------------------------------------- #

print("--------------------")
print("Subject1=",sub1)
print("Subject2=",sub2)
print("Subject3=",sub3)


if sub1>=40 and sub2>=40 and sub3>=40: #Root Condition

    print("--------------------")

    total=sub1+sub2+sub3
    print("Total:",total)

    print("--------------------")

    pr=total/3
    print("PR:",pr)
    print("--------------------")

    if pr>=70: #Child Condition
        print("Result:Dist.")
    elif pr>=60:
        print("Result:First Class")
    elif pr>=50:
        print("Result:Second Class")
    elif pr>=40:
        print("Result:Pass Class")
        
else:
    print("Result:FAIL")