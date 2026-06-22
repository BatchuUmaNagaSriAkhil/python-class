'''
find the absolute difference between first and last element in a list
i/p:[10,25,-30,-40]
o/p: 10-(-40)
'''
n = int(input())

a = list(map(int, input().split()))

diff = abs(a[0] - a[-1])

print(diff)