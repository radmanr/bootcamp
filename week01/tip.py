bill = float(input("Enter the bill amount: "))
tpercent = float(input("Enter tip percentage: "))
tip = bill * (tpercent/100)
print(f"The tip is: {round(tip, 2)} and the total is {round(bill + tip, 2)}")
