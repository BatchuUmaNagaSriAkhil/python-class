# Problem 5: Secret Number Door
# Problem Statement
# A digital door opens only if the entered number is equal to 7.
# The user gets maximum 3 attempts.
# If correct number is entered: Door Opened
# Otherwise: Access Denied
# Input Format
# Three integers representing user attempts
# Output Format
# Door Opened OR Access Denied
# Constraints
# 1 ≤ Number ≤ 100
# Sample Input
# 3
# 5
# 7
# Sample Output
# Door Opened

# Source Code:
# Read input values for three attempts
attempt1 = int(input("Enter first attempt: ")) 
attempt2 = int(input("Enter second attempt: "))
attempt3 = int(input("Enter third attempt: "))
# Check if any of the attempts is equal to 7
if attempt1 == 7 or attempt2 == 7 or attempt3 == 7:
    print("Door Opened")
else:
    print("Access Denied")