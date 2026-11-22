m=int(input("Enter the marks of Mathematics : "))
s=int(input("Enter the marks of Science : "))
e=int(input("Enter the marks of English : "))
average=(m+s+e)/3
print("Average : ",average)
if average>=75:
    print("Distinction")
elif average>=60 and average<=74:
    print("First class")
elif average>=40 and average<=59:
    print("Second class")
elif average<40:
    print("Fail")
else:
    print("Incorrect input")