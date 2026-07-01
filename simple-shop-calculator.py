products=[""]*3
amount=0
for i in range (3):
    products[i]=input("Enter a product name:")
    price=int(input("Enter the product price:"))
    amount=amount+price
#discount system
if (amount<100000):
    print(" your total amount is "+str(amount))
else:
    discount=(10/100)*amount 
    print("you qualify for a discount of: "+str(discount))
    amount=amount-discount
    print("your total amount is "+str(amount))