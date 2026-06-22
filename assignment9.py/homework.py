#Problem 1: Rotate Array by K Positions
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k %= n
arr = arr[-k:] + arr[:-k]

print(*arr)

#Problem 2: Find Missing Number
n = int(input())
arr = list(map(int, input().split()))

total = n * (n + 1) // 2
print(total - sum(arr))

#Problem 3: Maximum Difference Between Two Elements
n = int(input())
arr = list(map(int, input().split()))

min_ele = arr[0]
max_diff = arr[1] - arr[0]

for i in range(1, n):
    max_diff = max(max_diff, arr[i] - min_ele)
    min_ele = min(min_ele, arr[i])

print(max_diff)

#Problem 4: Check if Array is Sorted
n = int(input())
arr = list(map(int, input().split()))

flag = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        flag = False
        break

print("Sorted" if flag else "Not Sorted")

#Problem 5: Find Element Appearing Once
n = int(input())
arr = list(map(int, input().split()))

x = 0
for i in arr:
    x ^= i

print(x)