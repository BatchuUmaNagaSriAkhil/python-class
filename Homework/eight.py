# Problem 8: Train Ticket Fare Calculator
# Calculate train fare based on age category: Child (<12) → 50% fare; Adult (12–59)
# → Full fare; Senior citizen (60+) → 40% discount. Additional Rules: AC coach adds
# 30%; Festival season adds 10%.
# Concepts: Arithmetic operators, Conditional statements, Nested conditions
# Sample Input:
# Base Fare: 1000
# Age: 65
# AC Coach: yes
# Festival Season: yes
# Sample Output:
# Final Ticket Fare = 858.0

# Source Code:

# Input
base_fare = float(input("Base Fare: "))
age = int(input("Age: "))
ac_coach_input = input("AC Coach: ").lower()
festival_season_input = input("Festival Season: ").lower()

# Determine age-based fare
if age < 12:
    fare = base_fare * 0.5
elif age < 60:
    fare = base_fare
else:
    fare = base_fare * 0.6

# Additional charges
if ac_coach_input == "yes":
    fare += base_fare * 0.3
if festival_season_input == "yes":
    fare += base_fare * 0.1

# Output
print(f"Final Ticket Fare = {fare}")    