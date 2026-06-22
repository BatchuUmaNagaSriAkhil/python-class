# Problem 4: Water Bottle Tracker
# Problem Statement
# A fitness app tracks daily water intake.
# You are given:
# • Number of glasses consumed each hour
# Stop counting when total glasses become greater than or equal to 8.
# Input Format
# First line contains integer N
# Second line contains N integers
# Output Format
# Hours: X
# Water Intake: Y
# Constraints
# 1 ≤ N ≤ 24
# Sample Input
# 6
# 1 2 1 3 2 1
# Sample Output
# Hours: 5
# Water Intake: 9

# SOURCE CODE:
# Read input values
N = int(input("Enter number of hours: "))
glasses = list(map(int, input("Enter glasses consumed each hour: ").split()))
# Initialize counters
total_glasses = 0
hours = 0
# Loop through the glasses consumed each hour
for i in range(N):
    total_glasses += glasses[i]  # Add glasses consumed in the current hour
    hours += 1  # Increment hours counter
    if total_glasses >= 8:  # Check if total glasses is greater than or equal to 8
        break  # Stop counting if condition is met
# Print the results
print(f"Hours: {hours}")
print(f"Water Intake: {total_glasses}")
