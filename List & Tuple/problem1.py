'''
problem-8:
Find the largest odd number in a given list

'''
n = [1,2,3,4,5,6,7,8,9]
max = n[0]
for i in n:
    if i > max and i%2 != 0:
        max = i
print(max)