'''
find the smallest even number in a list

'''
n = int(input())
s1 = list(map(int, input().split()))
min = s1[1]
for i in s1:
    if min > i and i%2 == 0:
      min = i
print(min)
