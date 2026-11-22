age=int(input("Enter your age : "))
if age>=0 and age<=1:
    print("Infant")
elif age>=2 and age<=4:
    print("Toddler")
elif age>=5 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
elif age>=60:
    print("Senior")
else:
    print("Incorrect input")