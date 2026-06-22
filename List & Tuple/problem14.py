'''
count the numbers ending with 5
example:
input:[25,33,44,65]
output:2

'''
n = int(input())
s1 = list(map(int, input().split()))
count = 0
for i in s1:
    if i % 10 == 5:
        count += 1
print(count)