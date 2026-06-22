'''
Problem Statement
A puzzle game creates a zig-zag wave pattern using numbers.
Given an integer N, print numbers in the following way:
• 
• 
Odd rows should print numbers in increasing order
Even rows should print numbers in decreasing order
'''
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    if i % 2 != 0:
        for j in range(1, i + 1):
            print(j, end=" ")
    else:
        for j in range(i, 0, -1):
            print(j, end=" ")

    print()

   