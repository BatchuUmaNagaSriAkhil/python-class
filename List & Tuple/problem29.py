'''
sort the binary array:
i/p:[1,0,0,1,1,0,1]
o/p:[0,0,0,1,1,1,1]


'''
n = int(input())

a = list(map(int, input().split()))
a.sort()

print(*a)
