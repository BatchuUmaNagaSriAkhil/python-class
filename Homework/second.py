# Problem 2: Electricity Bill Generator
# Calculate electricity bill using the following conditions: First 100 units → ₹2/unit;
# Next 200 units → ₹5/unit; Above 300 units → ₹8/unit. If total bill exceeds ₹3000,
# add 10% surcharge.
# Concepts: Variables, Conditional statements, Arithmetic operators, Nested if
# Sample Input: Enter units: 450
# Sample Output:
# Electricity Bill = 3200
# Surcharge Applied
# Final Bill = 3520.0

# Source Code:

# Electricity Bill Generator

# Input number of units consumed
units = int(input("Enter units: "))

# Calculate electricity bill
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = (100 * 2) + ((units - 100) * 5)
else:
    bill = units * 8

print("Electricity Bill =", bill)

# Apply surcharge if bill exceeds 3000
if bill > 3000:
    print("Surcharge Applied")
    final_bill = bill + (bill * 0.10)
else:
    final_bill = bill

# Display final bill
print("Final Bill =", final_bill)