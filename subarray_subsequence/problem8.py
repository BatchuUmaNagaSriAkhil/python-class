#find the longest substring without repeating characters using sliding window approach with two pointers
s = input(" ")
a= set()
i = 0
max_len = 0

for j in range(len(s)):

    while s[j] in a:
        a.remove(s[i])
        i += 1

    a.add(s[j])

    max_len = max(max_len, j - i + 1)

print( max_len)