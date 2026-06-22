# problem statement:

#calculate the electricity bill using the conditions
#1. First 100 units --> 5/unit
#2. Next 100 units -->7/unit
#3. Above 200 units -->10/unit
units = int(input("Enter the units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print("Electricity Bill =", bill)               