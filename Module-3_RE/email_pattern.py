import re

email="sanket.chauhan2020@gmail.com"

email_pattern="^[a-z0-5._]+[@]+[a-z]+[.]+[a-z]{2,4}$"

x=re.findall(email_pattern,email)

if x:
    print("Email is valid")
else:
    print("Invalid Email!")