'''
arr = [2,1,5,1,3,2]
k = 3

1. 2 1 5 -->8
2. 1 5 1 -->7
3. 5 1 3 -->9
4. 1 3 2 -->6

'''
n = int(input())

a = list(map(int, input().split()))
k = int(input())
max_sum = 0
for i in range(n - k + 1):
    current_sum = sum(a[i:i + k])
    max_sum = max(max_sum, current_sum)
print(max_sum)

