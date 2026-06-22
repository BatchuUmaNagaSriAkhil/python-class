1. #Rainwater Storage Between Buildings (Trapping Rain Water)
n = int(input())
arr = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = arr[0]
for i in range(1, n):
    left[i] = max(left[i - 1], arr[i])

right[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    right[i] = max(right[i + 1], arr[i])

water = 0

for i in range(n):
    water += min(left[i], right[i]) - arr[i]

print(water)
'''
Input

6
3 0 0 2 0 4

Output

10

'''
