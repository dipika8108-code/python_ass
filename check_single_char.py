char=input("Enter single character value : ")
if char>="a" and char<="z":
    print("Character is of lowercase letter . ")
elif char>="A" and char<="Z":
    print("Character is of uppercase letter . ")
elif char>="0" and char<="9":
    print("Character is of digit . ")
else:
    print("Character is a special character . ")