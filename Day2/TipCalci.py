print("Welcome to the tip calculator")
total_bill= int(input("What is the total bill rs? "))
# print(total_bill)
tip = int(input("How much tip would you like to give? 10,12 or 15"))
people = int(input("How many people do you want to split the bill? "))

per_people_bill =  ( total_bill + (total_bill * (tip /100)) ) / people

print(f"Each person should pay : rs {per_people_bill} ")