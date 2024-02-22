print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage would you like to give? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
pay_each = total_bill / num_of_people
print(f"Each person should pay: {round(pay_each,2)}")
