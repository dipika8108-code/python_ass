num=int(input("Enter the number : "))
if num%2==0 and num>0:
    print("Number is positive even number.")
elif num%2!=0 and num>0:
    print("Number is positive odd number .")
elif num%2==0 and num<0:
    print("Number is negative even number.")
elif num%2!=0 and num<0:
    print("Number is negative odd number . ")
else:
    print("Number is zero.")
