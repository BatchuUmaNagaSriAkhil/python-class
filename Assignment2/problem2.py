# Problem 2: Mobile Battery Warning
# Problem Statement
# A mobile phone battery decreases every hour.
# You are given:
# • Initial battery percentage
# • Battery usage per hour
# Keep reducing battery until it becomes less than or equal to 20.
# Input Format
# First line contains integer battery
# Second line contains integer usage
# Output Format
# Hours: X
# Battery Left: Y
# Constraints
# 20 ≤ battery ≤ 100
# 1 ≤ usage ≤ 20
# Sample Input
# 100
# 15
# Sample Output
# Hours: 6
# Battery Left: 10

# Source Code:
# Read input values
battery = int(input("Enter initial battery percentage: "))
usage = int(input("Enter battery usage per hour: "))
# Initialize hours counter
hours = 0
# Loop until battery is less than or equal to 20
while battery > 20:
    battery -= usage  # Decrease battery by usage
    hours += 1  # Increment hours counter
# Print the results
print(f"Hours: {hours}")
print(f"Battery Left: {battery}")
