'''
reverse a list by two pointers approach
i/p:[1,2,3,4,5]
o/p:[5,4,3,2,1]

'''
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(*arr)