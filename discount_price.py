price=int(input("Enter product price : "))
if price>1000:
    discount=price*(10/100)
    final_price=price-discount
    print("Final price after applying  the discount : ",final_price)
elif price>=500 and price<=1000:
    discount=price*(5/100)
    final_price=price-discount
    print("Final price after applying  the discount : ",final_price)
else:
    print("There was no discount on price.")

    