'''
print the unique elements:
i/p:[1,2,2,3,4,4]
o/p:[1,3]
'''
n = int(input())

a = list(map(int, input().split()))
for i in a:
    if a.count(i) == 1:
        print(i)