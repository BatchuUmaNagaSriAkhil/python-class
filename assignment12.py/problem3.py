
#3. Nearest Restaurant Recommendations (K Closest Elements)
import bisect

n = int(input())
arr = list(map(int, input().split()))

k, x = map(int, input().split())

pos = bisect.bisect_left(arr, x)

left = pos - 1
right = pos

result = []

while k > 0:
    if left < 0:
        result.append(arr[right])
        right += 1

    elif right >= n:
        result.append(arr[left])
        left -= 1

    elif abs(arr[left] - x) <= abs(arr[right] - x):
        result.append(arr[left])
        left -= 1

    else:
        result.append(arr[right])
        right += 1

    k -= 1

result.sort()

print(*result)
'''
Input

7
1 2 3 4 5 6 7
3 5

Output

4 5 6
'''