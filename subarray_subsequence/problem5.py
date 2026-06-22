'''
find the first continuous subarray
whose sum equals to the target using sliding approach


arr = [1,4,20,3,10,5]


'''
n = int(input())
a = list(map(int, input().split()))
target = int(input())

i = 0
current_sum = 0

for j in range(n):
    current_sum += a[j]
    while current_sum > target and i <= j:
        current_sum -= a[i]
        i += 1
    if current_sum == target:
        for k in range(i, j + 1):
            print(a[k], end=" ")
        break
else:
        print("no subarray found")