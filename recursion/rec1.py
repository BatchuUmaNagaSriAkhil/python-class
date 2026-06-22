'''#find the largest element in an array using recursion
#I/P:[3,9,2,15,7]
#O/P:15
# Find the largest element in an array using recursion
'''
def find_largest(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_of_rest = find_largest(arr, n - 1)
        return max(arr[n - 1], max_of_rest)


arr = [3, 9, 2, 15, 7]
print(find_largest(arr, len(arr)))
'''
# check array is sorted or not using recursion
I/P:[1,2,3,4,5]
O/P:True
'''
def sorted(arr, n):
    if n == 1:
        return True
    else:
        return arr[n - 1] >= arr[n - 2] and sorted(arr, n - 1)

arr = [1, 2, 3, 4, 5]
print(sorted(arr, len(arr)))


