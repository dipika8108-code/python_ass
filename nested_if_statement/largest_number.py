num1=int(input("Enter the value of num_1 : "))
num2=int(input("Enter the value of num_2 : "))
num3=int(input("Enter the value of num_3 : "))
if num1>num2:
    if num1>num3:
        print("Number 1 is greater . " )
    else:
        print("Number 1 is smallar than others . ")
elif num2>num1:
    if num2>num3:
        print("Number 2 is greater . " )
    else:
        print("Number 2 is smallar than others . ")
else:
    print("Number 3 is greater . ")
    
