problem:3
t = int(input())
n = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()

    if len(a) == len(b) and b in (a + a):
        print("YES")
    else:
        print("NO")
'''I/P:
2
abcd
O/P:cdab
hello
llohe'''