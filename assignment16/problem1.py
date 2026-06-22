#Problem 1 — Recursive Array Product
n = int(input())
a = list(map(int, input().split()))

def product(i):
    if i == n:
        return 1
    return a[i] * product(i + 1)

print(product(0))