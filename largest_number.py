num1=int(input("Enter the value of num_1 : "))
num2=int(input("Enter the value of num_2 : "))
num3=int(input("Enter the value of num_3 : "))
if (num1>num2 and num1>num3):
    print(num1," is greater than others. ")
elif (num2>num3 and num2>num1):
    print(num2," is greater than others. ")
elif (num3>num1 and num3>num2):
    print(num3," is greater than others. ")
else:
    print("All number are equal")