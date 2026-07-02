products = [""] * 3
amount = 0

for i in range(3):
    products[i] = input("Enter a product name: ")

    while True:
        try:
            price = int(input("Enter the product price: "))
            if price >= 0:
                break
            else:
                print("Price cannot be negative.")
        except ValueError:
            print("Please enter numbers only.")

    amount += price

print("\nProducts Bought:")
for product in products:
    print(product)

if amount < 100000:
    print(f"\nYour total amount is: {amount:,} UGX")
else:
    discount = amount * 0.10
    final_amount = amount - discount

    print(f"\nYou qualify for a discount of: {discount:,.0f} UGX")
    print(f"Your total amount is: {final_amount:,.0f} UGX")
