#Problem 1 — Cyclic Iterator Sum
'''Problem Statement
Rahul creates an iterator for an array of integers and repeatedly accesses elements in cyclic
order. Given an array of size 
N and an integer 
K , print the sum of the first 
iterator restarts from the beginning after reaching the last element.'''
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    it = iter(a)
    s = 0
    cnt = 0

    for _ in range(k):
        if cnt == n:
            it = iter(a)
            cnt = 0

        s += next(it)
        cnt += 1

    print(s)