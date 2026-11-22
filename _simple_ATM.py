balance=10000
print(" Choose your choice : \n 1.CHECK BALANCE \n 2.DEPOSITE MONEY \n 3.WITHDRAW MONEY")
choice=int(input("Enter your choice : "))
if choice==1:
    print("Your account current balance is : ",balance)
elif choice==2:
    deposite=int(input("Your deposite amount : "))
    amount=balance+deposite
    print("Your balance is ",amount," after deposite")
elif choice==3:
    withdraw=int(input("Enter amount you want to withdraw : "))
    if withdraw<balance:
        amount=balance-withdraw
        print("Your balance is ",amount," after withdraw")
    else:
        print("Insufficient balance ! ")
else:
    print("Incorrect input")
    
    