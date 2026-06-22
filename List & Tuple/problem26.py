'''
using two pointers
'''

n = int(input())

a = list(map(int, input().split()))

target = int(input())
left = 0
right = len(a) - 1
while left < right:
    current_sum = a[left] + a[right]
    if current_sum == target:
        print(a[left], a[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1