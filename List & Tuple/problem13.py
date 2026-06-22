'''
find the difference between largest and smallest number in a list

'''
n =int(input())
s1 = list(map(int, input().split()))
max = s1[0]
min = s1[1]
for i in s1:
    if max <= i:
        max = i
    if min >i:
        min =i
ab = max-min
print(ab)