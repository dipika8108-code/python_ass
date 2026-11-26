a=int(input("Enter the first side of triangle : "))
b=int(input("Enter the second side of triangle : "))
c=int(input("Enter the third side of triangle : "))
if a+b>c or b+c>a or c+a>b:
    print("It is a valid triangle . ")
    if a==b==c:
        print("It is an equilateral triangle.")
    elif a==b or b==c or c==a:
        print("It is an isoscelens triangle.")
    else:
        print("It is an scalene triangle.")

else:
    print("It is not a valid triangle . ")
