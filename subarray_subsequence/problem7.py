'''
find the longest continous subarray
that contains no repeating elements using sliding window approach

Example:
input:[1,2,3,1,2,3,4]
output:4

'''

n = int(input())
arr = list(map(int, input().split()))

i = 0
seen = set()
max_len = 0
start = 0

for j in range(n):

    while arr[j] in seen:
        seen.remove(arr[i])
        i += 1

    seen.add(arr[j])

    if j - i + 1 > max_len:
        max_len = j - i + 1
        start = i

print(arr[start:start + max_len])
print(max_len)