import re

username="Sanket2020"

unm_pattern="^[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,username)

if x:
    print("Username is valid!")
else:
    print("Invalid Username")