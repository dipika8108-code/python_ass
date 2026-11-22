month=int(input(" Month number (1-12) : "))
if month==12 or month==1 or month==2:
    print("Winter season . ")
elif month==3 or month==4 or month==5:
    print("Spring season . ")
elif month==6 or month==7 or month==8:
    print("Summer season . ")
elif month==9 or month==10 or month==11:
    print("Autumn season . ")
else:
    print("Invalid month . ")