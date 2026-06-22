''' 
sum  of any two should be equal to target check all possible pairs
'''

n = int(input())

a = list(map(int, input().split()))

target = int(input())

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == target:
            print(a[i], a[j])

