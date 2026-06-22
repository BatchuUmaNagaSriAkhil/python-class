'''
A cricket player gains or loss points in each match
positive -> won points
negative ->lost points
 the coach wants to find the longest continuous winning streak with maximum points
 but insted of running sum,
 return the
 
 maximum score
 starting index
 ending index
 example

 Input:
 scores = [-2,4,-1,5,-3,2]
 output:
    maximum score = 8
    starting index = 1
    ending index = 3
    subarray = [4,-1,5]
'''
arr = [-2,4,-1,5,-3,2]
current_sum = arr[0]
max_sum = arr[0]
starting_index = 0
ending_index = 0
for i in range(1, len(arr)):
    if current_sum + arr[i] > arr[i]:
        current_sum += arr[i]
    else:
        current_sum = arr[i]
        starting_index = i
    if current_sum > max_sum:
        max_sum = current_sum
        ending_index = i
print(max_sum)
print(starting_index)
print(ending_index)
print(arr[starting_index:ending_index+1])