problem = 1

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    k %= n

    rotated = arr[n - k:] + arr[:n - k]
    print(*rotated)

'''
I/P:1
5 2
1 2 3 4 5
O/P:4 5 1 2 3
'''