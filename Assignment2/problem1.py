# Problem 1: Classroom Clap Counter
# Problem Statement
# During a school event, students clap after every performance.
# You are given:
# • Total number of performances N
# • Number of claps for each performance
# Find:
# 1. Total claps
# 2. Average claps per performance
# Input Format
# First line contains integer N
# Second line contains N space-separated integers
# Output Format
# Total Claps: X
# Average Claps: Y
# Constraints
# 1 ≤ N ≤ 100
# Sample Input
# 5
# 10 12 8 15 5
# Sample Output
# Total Claps: 50
# Average Claps: 10

#Source Code:

# Read the number of performances  
N = int(input("Enter the number of performances: "))
# Read the claps for each performance and convert them to a list of integers
claps = list(map(int, input("Enter the claps for each performance: ").split()))
# Calculate total claps
total_claps = sum(claps)
# Calculate average claps per performance
average_claps = total_claps / N
# Print the results
print(f"Total Claps: {total_claps}")
print(f"Average Claps: {average_claps:.2f}")