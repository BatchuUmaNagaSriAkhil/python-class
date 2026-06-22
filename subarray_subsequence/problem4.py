'''
find the first continuous subarray
whose sum equals to the target using sliding approach


arr = [1,4,20,3,10,5]


constraint: continuous subarray
1.elements should be adjacent
'''
arr = [1, 4, 20, 3, 10, 5]
target = 33

i = s = 0

for j in range(len(arr)):
    s += arr[j]

    while s > target:
        s -= arr[i]
        i += 1

    if s == target:
        print(arr[i:j+1])
        break