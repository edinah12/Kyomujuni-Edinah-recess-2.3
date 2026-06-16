#KYOMUJUNI EDINAH
#24/U/0617 

print("===== BILL SPLIT CALCULATOR =====")

# get and validate the total bill amount ensuring it is a postive value
while True:
    try:
        bill_amount = float(input("Enter total bill amount: "))
        if bill_amount > 0:
            break
        else:
            print("Bill amount must be greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

# get and validate the number of people sharing the bill making sure it is greater than zero
while True:
    try:
        num_people = int(input("Enter number of people: "))
        if num_people > 0:
            break
        else:
            print("Number of people must be at least 1.")
    except ValueError:
        print("Please enter a valid whole number.")

# allow the user to choose a tip percentage
print("\nTip Options:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Custom")

while True:
    choice = input("Choose tip option (1-4): ")

    if choice == "1":
        tip_percent = 10
        break
    elif choice == "2":
        tip_percent = 15
        break
    elif choice == "3":
        tip_percent = 20
        break
    elif choice == "4":
        while True:
            try:
                tip_percent = float(input("Enter custom tip percentage: "))
                if tip_percent >= 0:
                    break
                else:
                    print("Tip percentage cannot be negative.")
            except ValueError:
                print("Please enter a valid percentage.")
        break
    else:
        print("Invalid choice. Please select 1-4.")

# calculate tip amount, total bill and individual share
tip_amount = bill_amount * (tip_percent / 100)
total_bill = bill_amount + tip_amount
amount_per_person = total_bill / num_people

# display a detailled bill summary
print("\n" + "=" * 35)
print("            RECEIPT")
print("=" * 35)
print(f"Original Bill:      UGX {bill_amount:.2f}")
print(f"Tip Percentage:     {tip_percent:.1f}%")
print(f"Tip Amount:         UGX {tip_amount:.2f}")
print(f"Total Bill:         UGX {total_bill:.2f}")
print(f"Number of People:   {num_people}")
print("-" * 35)
print(f"Each Person Pays:   UGX {amount_per_person:.2f}")
print("=" * 35)