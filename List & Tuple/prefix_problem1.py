'''
find sum from 1 to 3

R = 3
L = 1


sum = pefix[3]-prefix[0]
sum = 14-2= 12

4+1+7 = 12


'''
#find the sum from 1 to 3

arr = [2,4,1,7,3]
L = 1
R = 3

prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    if i == 0:
        sum = arr[i]
    prefix[i] =prefix[i-1]+ arr[i]
print(prefix)
sum = prefix[R] -prefix[L-1]
print(sum)

