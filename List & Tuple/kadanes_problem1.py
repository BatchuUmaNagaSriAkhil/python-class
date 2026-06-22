'''
    maximum product subarray


    input:[2,3,-2,4]
    output:6     2*3
    '''
arr = [2,3,-2,4]
current_product = arr[0]
max_product = arr[0]
starting_index = 0
ending_index = 0
for i in range(1, len(arr)):
    if current_product * arr[i] > arr[i]:
        current_product *= arr[i]
    else:
        current_product = arr[i]
        starting_index = i
    if current_product > max_product:
        max_product = current_product
        ending_index = i
print(max_product)
print(starting_index)
print(ending_index)

