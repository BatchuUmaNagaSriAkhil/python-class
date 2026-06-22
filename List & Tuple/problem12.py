'''
find the number of elements greater than average value
input:[1,2,3,4,5]
avg=3
output:2
'''
n =int(input())
s1 = list(map(int, input().split()))
count = 0
average = sum(s1) / n
for i in s1:
    if average < i:
        count +=i
print(count)      