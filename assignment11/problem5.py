problem:5
t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    for k in range(1, n + 1):
        if s[k:] + s[:k] == s:
            print(k)
            break
'''
I/P:
2
abab
O/P:2
abc
3
'''