'''
find the equilibrium index  using prefix sum

arr = [1,3,5,2,2]         

'''
arr = [1,3,5,2,2]
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]
total_sum = prefix[-1]
equilibrium_index = 0
for i in range(len(arr)):
    left_sum = prefix[i] - arr[i]
    right_sum = total_sum - prefix[i]
    if  left_sum == right_sum:
        equilibrium_index = i
        break
print(equilibrium_index)
