# Problem 9: Fast Runner Detector
# Problem Statement
# A sports app records running speed for N students.
# Print:
# • "Fast" if speed is greater than or equal to 15
# • "Slow" otherwise
# Input Format
# First line contains integer N
# Second line contains N integers
# Output Format
# Print result for each student in separate line
# Constraints
# 1 ≤ N ≤ 100
# Sample Input
# 4
# 12 16 20 10
# Sample Output
# Slow
# Fast
# Fast
# Slow

# Source Code:
# Read input values
N = int(input("Enter number of students: "))
speeds = list(map(int, input("Enter running speeds of students: ").split()))
# Loop through the speeds and determine if each student is fast or slow
for speed in speeds:
    if speed >= 15:  # Check if speed is greater than or equal to 15
        print("Fast")  # Print "Fast" if condition is met
    else:
        print("Slow")  # Print "Slow" otherwise
        