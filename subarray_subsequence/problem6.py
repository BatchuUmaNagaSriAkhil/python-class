'''
find the longest continous subarray
that contains no repeating elements

Example:
input:[1,2,3,1,2,3,4]
output:4

'''
n = int(input())
a = list(map(int, input().split()))

max_len = 0

for i in range(n):
    seen = set()
    
    for j in range(i, n):
        if a[j] in seen:
            break
        
        seen.add(a[j])
        max_len = max(max_len, j - i + 1)

print(max_len)