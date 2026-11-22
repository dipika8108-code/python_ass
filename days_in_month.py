month=input("Enter the month : ")
day_31="january march may july august october december"
day_30="april june september november"
if month in day_31 :
    print("This month have 31 days ")
elif month in day_30:
    print("This month have 30 days")
elif month=="february":
    print("It is leap year. So,february have 29 days")
else:
    print("Incorrect input")
