'''
find the avg of numbers in a list
Note: Take the input from the user in a list



'''

n = int(input())

a = list(map(int, input().split()))

total = 0

for i in a:
    total += i

average = total / n

print(average)