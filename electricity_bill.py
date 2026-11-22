unit=float(input("Enter unit reading : "))
if unit<=100:
    bill=unit*5
    print("Bill : ",bill)
elif unit>=100 and unit<=200:
    bill=((unit-100)*7)+(100*5)
    print("Bill : ",bill)
elif unit>200:
    bill=((unit-200)*10)+(100*5)+(100*7)
    print("Bill : ",bill)
else:
    print("Recheck reading again ")
    
