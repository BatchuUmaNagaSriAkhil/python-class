'''
count the multiples of 3
i/p:[3,5,9,12,14]
o/p:3

'''
n = int(input())

a = list(map(int, input().split()))

count = 0

for i in a:
    if i % 3== 0:
        count += 1

print(count)