#Camilo Arciniegas

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_amount = total_tip_amount + bill
payment_amount = total_amount / people
final_amount = round(payment_amount, 2)

print(f"Every person needs to pay: {final_amount}")