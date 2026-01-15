print("Welcome to the tip calculator! \n")
bill = float(input("What was the total bill? \n"))
tip = int(input("How much tip would you like to give? 10, 12, 0r 15 \n"))
tip_percent = (tip/100) * bill
total_bill = bill + tip_percent
people = int(input("How many people to split the bill? \n"))
individual_bill = total_bill / people
rounding = round(individual_bill, 2)
print(f"Each person should pay £ {rounding}")
