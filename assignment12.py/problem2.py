
#2. Best Profit Streak Analyzer (Maximum Product Subarray)
n = int(input())
arr = list(map(int, input().split()))

max_prod = arr[0]
min_prod = arr[0]
ans = arr[0]

for i in range(1, n):
    if arr[i] < 0:
        max_prod, min_prod = min_prod, max_prod

    max_prod = max(arr[i], max_prod * arr[i])
    min_prod = min(arr[i], min_prod * arr[i])

    ans = max(ans, max_prod)

print(ans)
'''
Input

5
2 3 -2 4 -1

Output

48

Explanation:

2 × 3 × (-2) × 4 × (-1) = 48
'''
