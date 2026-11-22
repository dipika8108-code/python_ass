num=int(input("Enter the number : "))
if num%5==0 and num%3==0:
    print("Number is divisible by both 3 and 5 . ")
elif num%3==0:
    print("Number is only divisible by 3 . ")
elif num%5==0:
    print("Number is only divisible by 5 . ")
else:
    print("Number is not divisible by both 3 and 5 . ")