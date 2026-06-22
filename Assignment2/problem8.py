# Problem 8: Mini Shopping Bill
# Problem Statement
# A customer buys N items.
# You are given prices of all items.
# Find:
# 1. Total bill
# 2. Highest priced item
# Input Format
# First line contains integer N
# Second line contains N integers
# Output Format
# Total: X
# Highest: Y
# Constraints
# 1 ≤ N ≤ 100
# Sample Input
# 5
# 100 250 80 60 120
# Sample Output
# Total: 610
# Highest: 250

# SOURCE CODE:
# Read input values
N = int(input("Enter number of items: "))
prices = list(map(int, input("Enter prices of items: ").split()))
# Calculate total bill and highest priced item
total_bill = sum(prices)  # Calculate total bill by summing all prices
highest_price = max(prices)  # Find the highest priced item
# Print the results
print(f"Total: {total_bill}")
print(f"Highest: {highest_price}")