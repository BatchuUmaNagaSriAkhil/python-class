# Problem 3: Lucky Bus Ticket
# Problem Statement
# A bus conductor checks ticket numbers.
# A ticket is called lucky if:
# • It is divisible by both 3 and 5
# Given a ticket number N, determine whether it is lucky.
# Input Format
# Single integer N
# Output Format
# Lucky Ticket OR Not Lucky
# Constraints
# 1 ≤ N ≤ 10000
# Sample Input
# 30
# Sample Output
# Lucky Ticket

# Source Code:
# Read input value
ticket_number = int(input("Enter ticket number:"))
# Check if the ticket number is lucky
if ticket_number % 3 == 0 and ticket_number % 5 == 0:
    print("Lucky Ticket")
else:
    print("Not Lucky")