'''
Prefix Sum:One of the most important technique
used to solve sub array problems
1.Fast range sum queries
2.Optimization
3.Sliding window's alternative
4.Sub array problems
5.Competitive programming

It reduces the repeated calculations and 
improves the time complexity

what is prefix sum?
stores the cumulative sum of the elements
from the beginning of the array to every index

arr = [a0,a1,a2,a3....]

then:
prefix[i] = arr[0]+arr[1]+arr[2]+...arr[i]

problem:

arr = [2,4,1,7,3]
       0 1 2 3 4

find the sum from index 1 to 3



'''
'''
arr = [2,4,1,7,3]
sum = []
current_sum = 0
for num in arr:
    current_sum += num
    sum.append(current_sum)
print(sum[3]- sum[0])

'''
#no of queries can increase complexity


arr = [2,4,1,7,3]
L = 1
R = 3
total = 0

for i in range(L,R+1):
    total += arr[i]

print(total)

#find the sum from index 1 to 3 by prefix sum

'''
arr = [2,4,1,7,3]
       0 1 2 3 4

Caluculate the prefix:

index    arr[i]     prefix[i]
0           2           2
1           4           2+4=6
2           1           6+1=7
3           7           7+7=14
4           3           14+3=17

prefix[i] = [2,5,7,14,17]

prefix[0] = 2 sum from 0 to 0
prefix[1] = 6 sum from 0 to 1
prefix[2] = 7 sum from 0 to 2
prefix[3] = 14 sum from 0 to 3
prefix[4] = 17 sum from 0 to 4


prefix sum formula;
sum = prefix[R]-prefix[L-1]

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




