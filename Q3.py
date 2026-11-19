order_amount = float(input("Enter order amount: "))
membership = input("Are you a member? (yes/no): ").lower()

if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")

else:
    if order_amount >= 5000:
        discount_rate = 15

    elif membership == "yes" and order_amount >= 2000:
        discount_rate = 10

    else:
        discount_rate = 0

    discount_amount = order_amount * discount_rate / 100
    final_amount = order_amount - discount_amount

    print("Original amount:", order_amount)
    print("Discount percentage:", discount_rate, "%")
    print("Discount amount:", discount_amount)
    print("Final payable amount:", final_amount)

    if discount_rate > 0:
        print("Eligibility status: Eligible for discount")
    else:
        print("Eligibility status: Not eligible for discount")