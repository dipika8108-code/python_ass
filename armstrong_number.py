num=int(input("Enter three digit number : "))
d1=num//100
d2=(num//10)%10
d3=num%10
if(d1**3+d2**3+d3**3)==num:
    print(num," is a aramstrong number .")
else:
    print(num ," is not a aramstrong number . ")