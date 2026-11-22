a=int(input("Enter the first side of triangle : "))
b=int(input("Enter the second side of triangle : "))
c=int(input("Enter the third side of triangle : "))
if a+b>c:
    print("It is a valid triangle . ")
elif b+c>a:
    print("It is a valid triangle . ")
elif c+a>b:
    print("It is a valid triangle . ")
else:
    print("It is not a valid triangle . ")