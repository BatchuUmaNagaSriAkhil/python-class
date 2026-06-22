'''
move zeroes to the end of the list
i/p:[1,0,4,-2,0]
o/p:[1,4,-2,0,0]

'''
n = int(input())

a = list(map(int, input().split()))

i = 0 

for j in range(n):
    if a[j] != 0:
        a[i], a[j] = a[j], a[i]
        i += 1

print(*a)