print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percent 10, 15, or 12: "))
split_count = int(input("How many people will split the bill? "))
# division converts to float
# tip is .10
tip_as_percent = tip / 100
# tip is 10 added to bill
tip_amount = tip_as_percent * bill
# bill is 110
total_bill = tip_amount + bill
# 100 / 5 is 20
amount_per_person = total_bill / split_count
# round it to $20.00
amount = round(amount_per_person, 2)


print(f"Each person should pay: {amount}")
