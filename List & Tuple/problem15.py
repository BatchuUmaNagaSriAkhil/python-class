'''
replace the negative numbers with zeros
'''
n =int(input())
s1 = list(map(int, input().split()))
for i in range(n):
    if s1[i] < 0:
        s1[i] = 0
print(s1)