problem = 2

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1

    if count <= 1:
        print("YES")
    else:
        print("NO")
'''
I/P:
2
5
3 4 5 1 2
O/P:YES
I/P:5
3 5 4 1 2
'''