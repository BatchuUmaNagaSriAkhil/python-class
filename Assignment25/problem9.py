#Product of Non-Zero Elements
from math import prod

n = int(input())
arr = list(map(int, input().split()))

nums = [x for x in arr if x != 0]

print(prod(nums) if nums else 0)