

#Missing Badge Detection
n = int(input())
ids = list(map(int, input().split()))

freq = {}

# Count frequencies
for i in ids:
    freq[i] = freq.get(i, 0) + 1

result = []

# Find IDs appearing exactly once
for key, value in freq.items():
    if value == 1:
        result.append(key)

result.sort()

print(*result)