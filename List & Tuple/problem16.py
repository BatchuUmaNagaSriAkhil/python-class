'''
product of all the elements in a list
'''


n = int(input())
s1 = list(map(int, input().split()))

product = 1

for i in s1:
    product = product * i

print(product)