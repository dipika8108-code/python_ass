print("1.KILOMETERS TO MILES.\n2.CELSIUS TO FAHRENHEIT.\n3.KILOGRAMS TO POUNDS.")
choice=int(input("Enter your choice : "))
value=float(input("Enter the value : "))
if choice==1:
    miles=value*0.621371
    print("Miles = ",miles)
elif choice==2:
    fahrenheit=(value*9)/5+32
    print("Fahrenheit = ",fahrenheit)
elif choice==3:
    pounds=value*2.20462
    print("Pounds = ",pounds)
else:
    print("Invalid choice")