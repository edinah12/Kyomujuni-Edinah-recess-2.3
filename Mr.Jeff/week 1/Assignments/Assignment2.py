
# E-COMMERCE SYSTEM
# Login, Discounts, Taxes, and Receipt

# User Database
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

print(" E-COMMERCE LOGIN ")

# Login Inputs
username = input("Enter Username: ")
password = input("Enter Password: ")

# Authentication
if username in users:

    if users[username]["password"] == password:

        role = users[username]["role"]

        print("\nLogin Successful!")
        print("Role:", role)

        # Role-Based Access
        if role == "Admin":
            print("Access: Full System Control")

        elif role == "Cashier":
            print("Access: Sales and Billing")

        elif role == "Customer":
            print("Access: Purchase Products")


        # PRODUCT PURCHASE SECTION

        print("\n PRODUCT PURCHASE ")

        subtotal = float(input("Enter Product Subtotal: "))

        # Coupon Code
        coupon = input(
            "Enter Coupon Code (SAVE10, SAVE20, NONE): "
        ).upper()

        coupon_discount = 0

        # Nested Conditions
        if coupon == "SAVE10":

            coupon_discount = subtotal * 0.10

        elif coupon == "SAVE20":

            if subtotal >= 100:
                coupon_discount = subtotal * 0.20
            else:
                print(
                    "SAVE20 only applies to purchases of 100 or more."
                )

        elif coupon == "NONE":
            coupon_discount = 0

        else:
            print("Invalid Coupon Code!")
            coupon_discount = 0

        # Amount after coupon discount
        amount_after_coupon = subtotal - coupon_discount

        # EXTRA DISCOUNTS
    
        extra_discount = 0

        if subtotal >= 500:

            extra_discount = amount_after_coupon * 0.05
            print("Extra 5% Premium Discount Applied!")

        elif subtotal >= 200:

            extra_discount = amount_after_coupon * 0.02
            print("Extra 2% Discount Applied!")

        # Amount after all discounts
        amount_before_tax = amount_after_coupon - extra_discount

        
        # LOCATION TAX
    
        print("\nLocations")
        print("1. Uganda")
        print("2. Kenya")
        print("3. Tanzania")

        location = input("Choose Location: ")

        tax_rate = 0

        if location == "1":
            tax_rate = 0.18

        elif location == "2":
            tax_rate = 0.16

        elif location == "3":
            tax_rate = 0.18

        else:
            print("Invalid Location!")
            tax_rate = 0

        # Tax Calculation
        tax = amount_before_tax * tax_rate

        # Final Price
        final_price = amount_before_tax + tax


        # RECEIPT
        print("\n RECEIPT ")

        print(f"Subtotal: {subtotal:.2f}")
        print(f"Coupon Discount: {coupon_discount:.2f}")
        print(f"Extra Discount: {extra_discount:.2f}")
        print(f"Amount Before Tax: {amount_before_tax:.2f}")
        print(f"Tax: {tax:.2f}")
        print(f"Final Price: {final_price:.2f}")

    else:
        print("Incorrect Password!")

else:
    print("User Not Found!")