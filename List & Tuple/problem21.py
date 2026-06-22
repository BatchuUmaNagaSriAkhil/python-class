'''
move all the negative numbers to the left 
given a list of integers,move all the negative numbers
to the begining of the list
Note: maintain the order
'''
n = int(input())

a = list(map(int, input().split()))

neg = []
pos = []

for num in a:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

result = neg + pos

print(*result)