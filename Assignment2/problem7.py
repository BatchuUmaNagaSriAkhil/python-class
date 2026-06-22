# Problem 7: Skipping Broken Steps
# Problem Statement
# A child climbs stairs numbered from 1 to N.
# Some steps are broken:
# • Multiples of 4 are broken
# Print all safe steps.
# Input Format
# Single integer N
# Output Format
# Print safe step numbers
# Constraints
# 1 ≤ N ≤ 100
# Sample Input
# 10
# Sample Output
# 1 2 3 5 6 7 9 10

# Source Code:
# Read input value
N = int(input("Enter the number of steps: "))
# Loop through numbers from 1 to N and print safe steps
for i in range(1, N + 1):
    if i % 4 != 0:  # Check if the step is not a multiple of 4 (not broken)
        print(i, end=' ')  # Print the safe step followed by a space
print()  # Print a newline at the end
