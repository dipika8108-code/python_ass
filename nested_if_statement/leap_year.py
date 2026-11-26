year=int(input("Enter the year"))
if (year%4==0 and year%100!=0):
    if year%400==0:
        print("not a leap year")
    else:
        print(year,"is a leap year.")
else:
    print("Not a leap year")
