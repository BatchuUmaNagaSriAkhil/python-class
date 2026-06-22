'''
find all the odd numbers in a list
Note: take the list as input from user
'''
n = int(input())

a = list(map(int, input().split()))

print("Odd numbers are:")

for i in a:
    if i% 2 != 0:
        print(i, end=" ")