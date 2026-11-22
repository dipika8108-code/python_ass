weight=float(input("Enter your weight : "))
height=float(input("Enter your height : "))
BMI=(weight/(height**2))
print(BMI)
if BMI<18.5:
    print("Your BMI  condition is underweight .")
elif BMI>=18.5 and BMI<24.9:
    print("Your BMI condition is Normal weight . ")
elif BMI>=25 and BMI<29.9:
    print("Your BMI condition is Overweight . ")
elif BMI>=30:
    print("Your BMI condition is obesity.")
else:
    print("Incorrect input")