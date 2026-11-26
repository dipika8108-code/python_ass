marks=int(input("Enter your marks : "))
if marks>=0 and marks<=100:
    if marks<100 and marks>=90:
        print("Grade A")
    elif marks<90 and marks>=75:
        print("Grade B")
    elif marks<75 and marks>=50:
        print("Grade C")
    else :
        print("Garde F")
else:
    print("Invalid marks")
