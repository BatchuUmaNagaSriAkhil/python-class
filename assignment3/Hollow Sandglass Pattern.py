'''Problem Statement
A game engine generates a hollow sandglass structure using stars.
Given an integer N, print a hollow sandglass pattern.
Rules:
• 
• 
• 
Only outer boundary stars should be printed
Inner region should contain spaces
Upper and lower halves must be symmetric'''

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(" " * i, end="")
    
    for j in range(n - i):
        if i == 0 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()
for i in range(n-2, -1, -1):
    print(" " * i, end="")
    
    for j in range(n - i):
        if i == 0 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()