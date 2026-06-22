#1. Split Array Largest Sum
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

low = max(nums)
high = sum(nums)

while low < high:
    mid = (low + high) // 2

    count = 1
    curr = 0

    for num in nums:
        if curr + num > mid:
            count += 1
            curr = num
        else:
            curr += num

    if count <= k:
        high = mid
    else:
        low = mid + 1

print(low)

#2. Maximum Sum of 3 Non-Overlapping Subarrays
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

m = n - k + 1

window = [0] * m
curr = sum(nums[:k])
window[0] = curr

for i in range(1, m):
    curr += nums[i + k - 1] - nums[i - 1]
    window[i] = curr

left = [0] * m
best = 0

for i in range(m):
    if window[i] > window[best]:
        best = i
    left[i] = best

right = [0] * m
best = m - 1

for i in range(m - 1, -1, -1):
    if window[i] >= window[best]:
        best = i
    right[i] = best

ans = [-1, -1, -1]
max_sum = 0

for mid in range(k, m - k):
    l = left[mid - k]
    r = right[mid + k]

    total = window[l] + window[mid] + window[r]

    if total > max_sum:
        max_sum = total
        ans = [l, mid, r]

print(*ans)

#3. Sliding Window Median
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

medians = []

for i in range(n - k + 1):
    window = sorted(nums[i:i+k])

    if k % 2:
        medians.append(str(window[k // 2]))
    else:
        median = (window[k//2 - 1] + window[k//2]) / 2
        medians.append(str(median))

print(*medians)