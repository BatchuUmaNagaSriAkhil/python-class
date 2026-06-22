# Problem 10: Loop Meter
# Problem Statement
# Given a value N, print numbers from 1 to N.
# Also print:
# • Total iterations executed
# Input Format
# Single integer N
# Output Format
# 1 2 3 4 5
# Iterations: 5
# Constraints
# 1 ≤ N ≤ 1000
# Sample Input
# 5
# Sample Output
# 1 2 3 4 5
# Iterations: 5

# Source Code:
# Read input value
N = int(input("Enter a value for N: "))
# Loop through numbers from 1 to N and print them
for i in range(1, N + 1):
    print(i, end=' ')  # Print the number followed by a space
print()  # Print a newline at the end
# Print the total iterations executed
print("Iterations: ",N)  # The number of iterations is equal to N
