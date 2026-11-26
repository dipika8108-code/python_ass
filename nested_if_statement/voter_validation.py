age=int(input("Enter the age : "))
if age>=18:

    print("user age is above 18 . ")
    vote_id=input("User have voter id card (Yes/No) : ")
    if vote_id=="Yes":
        print("User allowed to vote . ")
    else:
        print("User required voter id . ")
else:
    print("user is not eligible for vote")
