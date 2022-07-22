def user_signup(fnm,lnm,email,password):
    print("Firstname:",fnm)
    print("Lastname:",lnm)
    print("Email:",email)
    print("Password:",password)

#user_signup("Sanket","Chauhan","sanket@gmail.com","tops?123")

firstname=input("Enter Firstname:")
lastname=input("Enter Lastname:")
email=input("Enter Email:")
password=input("Enter Password:")

user_signup(firstname,lastname,email,password)

