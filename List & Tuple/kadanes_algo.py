'''
kadanes algorithm : Max sub arrays problems

arr = [2,-1,3,-2,4]

find the contigious subarray with max sum

subarray: [-1,3,-2] right
          [2,3] invalid

subarrays   sum
[2]          2
[2,-1]       1
[2,-1,3]     4
[2,-1,3,-2]  2
[2,-1,3,-2,4]6

i = 1
[-1]         1
[-1,3]       2
[-1,3,-2]    0



At every element we decide 2 elements

Two choices
        1.continue & previous array

                (or)

        2.Start a new array

current_sum = -5
next_element = 10

-5+10 = 5 #discarding the previous (-ve)
next == 10

arr = [2,-1,3,-2,4]

current_sum = 2
max_sum = 2

index-1:
    -1
    choice-1: extend the array
    2+(-1)= 1

    choice-2: start a new array
    -1

current_sum = 1
max_sum = 2

index-2: 3

  choice-1: extend the array
    2+(-1)= 1+3=4

    choice-2: start a new array
    3

current_sum = 4
max_sum = max(2,4) =4

index-3: -2

  choice-1: extend the array
    2+(-1)= 1+3=4+(-2) = 2

    choice-2: start a new array
    -2
current_sum = max(4,2) = 4
max_sum = max(4,4) = 4

index-4: 4

  choice-1: extend the array
    2+(-1)= 1+3=4-2=2+4=6

    choice-2: start a new array
    4
current_sum = 6
max_sum = max(4,6) = 6

current_sum = max(arr[i],current_sum+arr[i])
max_sum = max(max_sum,current_sum)

'''

arr = [2,-1,3,-2,4]
current_sum = arr[0]
max_sum = arr[0]
for i in range(1, len(arr)):
    current_sum = max(arr[i],current_sum+arr[i])
    max_sum = max(max_sum,current_sum)
print(max_sum)


