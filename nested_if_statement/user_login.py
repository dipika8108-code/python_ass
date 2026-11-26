user=input("Enter the user name : ")
if user=="admin":
    password=input("Enter the password : ")
    if password=="1234":
        print("Login successful ....")
    else:
        ("Wrong password")
else:
    print("User not found . ")
