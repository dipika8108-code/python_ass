hour=int(input("Enter the hour person worked in a week  : "))
if hour<=40:
    salary=hour*200
    print("Person Salary : ",salary)
elif hour>41 and hour<=60:
    salary=((hour-40)*300)+(40*200)
    print("Person Salary : ",salary)
elif hour>60:
    print("Person overtime limit exceeded")
else:
    print("Incorrect input")
    
    