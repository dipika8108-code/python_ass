choice=input("Enter your choice (+,-,*,//,%,/,**) : ")
num1=int(input("Enter the value of num_1 : "))
num2=int(input("Enter the value of num_2 : "))
if choice=="+":
    sum=num1+num2
    print("Addition : ",sum)
elif choice=="-":
    sub=num1-num2
    print("Subtraction : ",sub)
elif choice=="*":
    mul=num1*num2
    print("Multiplication : ",mul)
elif choice=="//":
    a=num1//num2
    print("Floor division : ",a)
elif choice=="%":
    mod=num1%num2
    print("Module : ",mod)
elif choice=="/":
    div=num1/num2
    print("Division : ",div)
elif choice=="-":
    pow=num1**num2
    print("Exponent : ",pow)
else:
    print("Incorrect choice")