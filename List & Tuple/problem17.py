'''
print the elements greater than previous element

input:2 5 3 8 6

5>2 --->yes
3>5 --->no
8>3 --->yes
6>8 --->no

output: 5 8

'''
nums = (input())

nums = list(map(int, input().split()))

for i in range(1,len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i], end=" ")
    