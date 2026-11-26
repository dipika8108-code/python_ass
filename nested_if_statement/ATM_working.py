balance=int(input("Enter your account balance : "))
amount=int(input("Enter the withdraw amount  : "))
if amount>0:
    if amount%100==0 and amount<=balance:
        print("You can withdraw amount from your account . ")
    else:
        print("You cannot withdraw as you have not suffiecient account . ")
else:
    print("Invalid withdraw amount . ")
