# Problem 6: Candy Box Counter
# Problem Statement
# A candy box contains candies numbered from 1 to N.
# Print only even numbered candies.
# Input Format
# Single integer N
# Output Format
# Print all even numbers from 1 to N
# Constraints
# 1 ≤ N ≤ 100
# Sample Input
# 10
# Sample Output
# 2 4 6 8 10

# Source Code:
# Read input value
N = int(input("Enter the number of candies: "))
# Loop through numbers from 1 to N and print even numbers
for i in range(1, N + 1):
    if i % 2 == 0:  # Check if the number is even
        print(i, end=' ')  # Print the even number followed by a space
print()  # Print a newline at the end
