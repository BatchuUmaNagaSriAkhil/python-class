'''
find the firstcontinuous subarray
whose sum equals to the target


arr = [1,4,20,3,10,5]


constraint: continuous subarray
1.elements should be adjacent
'''
n = int(input())
a = list(map(int, input().split()))
k = int(input())

i = s = 0
for j in range(n):
    s += a[j]
    while s > k:
        s -= a[i]
        i += 1
    if s == k:
        print(a[i:j+1])
        break
else:
    print("Not found")