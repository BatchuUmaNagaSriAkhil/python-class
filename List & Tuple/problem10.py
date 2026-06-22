'''
find the sum of the digits of each element in a list

Example:
input:[10,23,33,45,56]

output:[1,5,6,9,11]
'''
n = int(input())

a = list(map(int, input().split()))

result = []

for i in range(n):
    num = a[i]
    digit_sum = 0

    while num > 0:
        digit_sum += num % 10
        num = num // 10

    result.append(digit_sum)                    

print(result)