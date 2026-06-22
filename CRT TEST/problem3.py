n = input().strip()
l = {}
left = 0
max_len = 0
for right in range(len(n)):
    if n[right] in l and l[n[right]] >= left:
        left = l[n[right]] + 1
    l[n[right]] = right
    max_len = max(max_len,right - left + 1)
print(max_len)