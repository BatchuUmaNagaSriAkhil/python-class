'''
Problem 3: A company generates employee IDs as numbers. An ID is considered special if it is 
divisible by both 3 and 5.
Given a range of numbers from 1 to N, find how many special IDs are present.
Input Format
A single integer N.
Output Format
Print the count of special numbers between 1 and N (inclusive).
'''
n = int(input())
id = list(map(int,input().split()))
special = 0
for i in id:
    if i%3 == 0 and i%5 == 0:
        special += 1
    else:
        pass    
print(special)