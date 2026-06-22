'''
rotate list by k positions
given a list & k integers, rotate the
list to the left by k positions
Example:
input:[1,2,3,4,5]
k = 2
o/p:[4,5,1,2,3]
'''
n = int(input())

a = list(map(int, input().split()))

k = int(input())

k = k % n

result = a[-k:] + a[:-k]

print(*result)
