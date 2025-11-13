print("Welcome To Tip Calculator!")
bill = float(input("What was the total bill? Rs."))
tip = int(input("How much tip would you like to give in percentage? 5, 10, or 12? "))
total = bill + (bill*tip/100)
split = int(input("How many people to split the bill? "))
bill_per_person = total/split
total_bill = round(bill_per_person,2)
print(f"Each person should pay : Rs.{total_bill}")
